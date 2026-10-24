"""EOS-005: Enterprise Scheduler for DynamiCore.

Compatibility:
    submit_task(task_id, operation, priority="NORMAL")
    next_task()
    queue_status()
    history()
    diagnostics()

Scheduling is explicit and synchronous. This component does not start
background workers or execute arbitrary operation strings.
"""
from __future__ import annotations

import json
import os
import tempfile
import threading
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


class EnterpriseScheduler:
    VERSION = "EOS-005"
    PRIORITY_ORDER = {
        "CRITICAL": 0,
        "HIGH": 1,
        "NORMAL": 2,
        "LOW": 3,
    }
    TERMINAL_STATES = {"COMPLETED", "FAILED", "CANCELLED"}

    def __init__(self, storage_path=None, event_bus=None):
        self.queue = []
        self.history_records = []
        self.event_bus = event_bus
        self.storage_path = Path(storage_path) if storage_path else None
        self._lock = threading.RLock()
        self._handlers: dict[str, Callable[[Any], Any]] = {}
        self._idempotency = {}
        if self.storage_path is not None:
            self._load()

    @staticmethod
    def _timestamp():
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _priority_key(value):
        if isinstance(value, str):
            upper = value.upper()
            if upper not in EnterpriseScheduler.PRIORITY_ORDER:
                raise ValueError(
                    "priority must be CRITICAL, HIGH, NORMAL, or LOW"
                )
            return EnterpriseScheduler.PRIORITY_ORDER[upper]
        if isinstance(value, int) and not isinstance(value, bool):
            return -value
        raise TypeError("priority must be a supported string or integer")

    def register_handler(self, operation, handler):
        if not isinstance(operation, str) or not operation:
            raise ValueError("operation must be a non-empty string")
        if not callable(handler):
            raise TypeError("handler must be callable")
        with self._lock:
            self._handlers[operation] = handler

    def submit_task(
        self,
        task_id,
        operation,
        priority="NORMAL",
        *,
        run_at=None,
        payload=None,
        max_attempts=1,
        idempotency_key=None,
    ):
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("task_id must be a non-empty string")
        if not isinstance(operation, str) or not operation:
            raise ValueError("operation must be a non-empty string")
        self._priority_key(priority)
        if not isinstance(max_attempts, int) or max_attempts < 1:
            raise ValueError("max_attempts must be an integer >= 1")

        # Validate persistability before changing in-memory state.
        json.dumps(payload)
        due_time = time.time() if run_at is None else float(run_at)

        with self._lock:
            if idempotency_key and idempotency_key in self._idempotency:
                return dict(self._idempotency[idempotency_key])

            if any(
                t["task_id"] == task_id
                for t in self.queue + self.history_records
            ):
                raise ValueError(f"task_id already exists: {task_id}")

            now = time.time()
            task = {
                "schedule_id": str(uuid.uuid4()),
                "task_id": task_id,
                "operation": operation,
                "priority": priority,
                "status": "QUEUED",
                "created": self._timestamp(),
                "updated": self._timestamp(),
                "run_at": due_time,
                "payload": payload,
                "attempts": 0,
                "max_attempts": max_attempts,
                "idempotency_key": idempotency_key,
                "result": None,
                "last_error": None,
                "version": self.VERSION,
            }
            self.queue.append(task)
            if idempotency_key:
                self._idempotency[idempotency_key] = task
            self._save()
            self._emit("scheduler.task_queued", task)
            return dict(task)

    def next_task(self, *, now=None):
        """Reserve and return one due task; does not execute it."""
        with self._lock:
            current = time.time() if now is None else float(now)
            due = [t for t in self.queue if t["run_at"] <= current]
            if not due:
                return {"status": "EMPTY"}

            task = min(
                due,
                key=lambda t: (
                    self._priority_key(t["priority"]),
                    t["run_at"],
                    t["created"],
                    t["task_id"],
                ),
            )
            self.queue.remove(task)
            task["status"] = "SCHEDULED"
            task["updated"] = self._timestamp()
            self.history_records.append(task)
            self._save()
            self._emit("scheduler.task_scheduled", task)
            return dict(task)

    def execute_next(self, *, now=None):
        """Execute one due task through its registered operation handler."""
        task = self.next_task(now=now)
        if task.get("status") == "EMPTY":
            return task

        with self._lock:
            record = self._find_history(task["task_id"])
            if record is None:
                raise RuntimeError("Scheduled task record disappeared")
            handler = self._handlers.get(record["operation"])
            record["attempts"] += 1
            record["status"] = "RUNNING"
            record["updated"] = self._timestamp()
            self._save()

        try:
            if handler is None:
                raise LookupError(
                    f"No handler registered for operation: {record['operation']}"
                )
            result = handler(record["payload"])
            json.dumps(result)
            with self._lock:
                record["result"] = result
                record["status"] = "COMPLETED"
                record["last_error"] = None
                record["updated"] = self._timestamp()
                self._save()
                self._emit("scheduler.task_completed", record)
                return dict(record)
        except Exception as exc:
            with self._lock:
                record["last_error"] = f"{type(exc).__name__}: {exc}"
                record["updated"] = self._timestamp()
                if record["attempts"] < record["max_attempts"]:
                    record["status"] = "QUEUED"
                    record["run_at"] = time.time()
                    self.history_records.remove(record)
                    self.queue.append(record)
                    outcome = dict(record)
                    event = "scheduler.task_retry"
                else:
                    record["status"] = "FAILED"
                    outcome = dict(record)
                    event = "scheduler.task_failed"
                self._save()
                self._emit(event, record)
                return outcome

    def cancel(self, task_id):
        with self._lock:
            for task in self.queue:
                if task["task_id"] == task_id:
                    self.queue.remove(task)
                    task["status"] = "CANCELLED"
                    task["updated"] = self._timestamp()
                    self.history_records.append(task)
                    self._save()
                    self._emit("scheduler.task_cancelled", task)
                    return True
            return False

    def queue_status(self):
        with self._lock:
            return [dict(t) for t in self.queue]

    def history(self):
        with self._lock:
            return [dict(t) for t in self.history_records]

    def diagnostics(self):
        with self._lock:
            states = {}
            for task in self.queue + self.history_records:
                states[task["status"]] = states.get(task["status"], 0) + 1
            return {
                "version": self.VERSION,
                "queued_tasks": len(self.queue),
                "scheduled_tasks": sum(
                    1 for t in self.history_records
                    if t["status"] == "SCHEDULED"
                ),
                "completed_tasks": states.get("COMPLETED", 0),
                "failed_tasks": states.get("FAILED", 0),
                "cancelled_tasks": states.get("CANCELLED", 0),
                "states": states,
                "persistent": self.storage_path is not None,
                "status": "READY",
            }

    def _find_history(self, task_id):
        return next(
            (t for t in self.history_records if t["task_id"] == task_id),
            None,
        )

    def _emit(self, event_type, task):
        if self.event_bus is not None:
            self.event_bus.publish(event_type, dict(task))

    def _load(self):
        if not self.storage_path.exists():
            return
        document = json.loads(
            self.storage_path.read_text(encoding="utf-8")
        )
        if document.get("schema_version") != 1:
            raise ValueError("Unsupported scheduler persistence schema")
        self.queue = document.get("queue", [])
        self.history_records = document.get("history", [])
        self._idempotency = {
            t["idempotency_key"]: t
            for t in self.queue + self.history_records
            if t.get("idempotency_key")
        }
        # A process may have stopped while a handler was running.
        # Do not automatically replay uncertain side effects.
        for task in self.history_records:
            if task.get("status") == "RUNNING":
                task["status"] = "FAILED"
                task["last_error"] = (
                    "Interrupted while RUNNING; manual reconciliation required"
                )
        self._save()

    def _save(self):
        if self.storage_path is None:
            return
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        document = {
            "schema_version": 1,
            "version": self.VERSION,
            "updated_at": self._timestamp(),
            "queue": self.queue,
            "history": self.history_records,
        }
        fd, temp_name = tempfile.mkstemp(
            prefix=self.storage_path.name + ".",
            suffix=".tmp",
            dir=str(self.storage_path.parent),
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                json.dump(document, stream, ensure_ascii=False, indent=2)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temp_name, self.storage_path)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)


# Short alias for consumers that prefer the generic name.
Scheduler = EnterpriseScheduler
