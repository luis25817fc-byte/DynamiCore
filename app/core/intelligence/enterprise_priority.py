from enum import IntEnum


class EnterprisePriority(IntEnum):

    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4
    EMERGENCY = 5


def normalize_priority(priority):

    if isinstance(priority, EnterprisePriority):
        return priority

    return EnterprisePriority.NORMAL