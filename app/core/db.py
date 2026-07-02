import sqlite3

DB_NAME = "dynamicore.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_key TEXT UNIQUE,
        requests INTEGER DEFAULT 0,
        limit_requests INTEGER DEFAULT 1000
    )
    """)

    conn.commit()
    conn.close()


def get_user(api_key):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE api_key=?", (api_key,))
    user = c.fetchone()

    conn.close()
    return user


def create_user(api_key):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (api_key, requests, limit_requests) VALUES (?, 0, 1000)",
        (api_key,)
    )

    conn.commit()
    conn.close()


def increment(api_key):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "UPDATE users SET requests = requests + 1 WHERE api_key=?",
        (api_key,)
    )

    conn.commit()
    conn.close()
