import sqlite3

DB = "dynamicore.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        api_key TEXT UNIQUE,
        plan TEXT DEFAULT 'free',
        requests INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def create_user(api_key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (api_key, plan, requests) VALUES (?, 'free', 0)",
        (api_key,)
    )

    conn.commit()
    conn.close()


def get_user(api_key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE api_key=?", (api_key,))
    user = c.fetchone()

    conn.close()
    return user


def upgrade_user(api_key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("UPDATE users SET plan='pro' WHERE api_key=?", (api_key,))

    conn.commit()
    conn.close()


def increment(api_key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("UPDATE users SET requests = requests + 1 WHERE api_key=?", (api_key,))

    conn.commit()
    conn.close()
