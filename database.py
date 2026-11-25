import sqlite3
from datetime import date

DB_PATH = "bot.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT DEFAULT '',
            first_name TEXT DEFAULT '',
            lesson_index INTEGER DEFAULT 0,
            score INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            best_streak INTEGER DEFAULT 0,
            xp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS exercises (
            user_id INTEGER,
            lesson_index INTEGER,
            exercise_index INTEGER,
            status TEXT DEFAULT 'locked',
            submitted_code TEXT DEFAULT '',
            output TEXT DEFAULT '',
            completed_at TEXT
        );
    """)
    conn.commit()
    conn.close()


def get_or_create_user(user_id, username=None, first_name=None):
    conn = get_connection()
    cur = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?)",
            (user_id, username or "", first_name or ""),
        )
        conn.commit()
    conn.close()
    return get_user(user_id)


def get_user(user_id):
    conn = get_connection()
    try:
        cur = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
    except sqlite3.OperationalError:
        conn.close()
        init_db()
        return get_user(user_id)
    if row:
        result = dict(row)
        # Добавляем поля если их нет (старая схема)
        for key in ['lesson_index', 'xp', 'level']:
            if key not in result:
                result[key] = 0 if key != 'level' else 1
        return result
    return None


def update_user_progress(user_id, lesson_index: int, xp_earned: int):
    conn = get_connection()
    user = get_user(user_id)
    if user is None:
        user = get_or_create_user(user_id)

    new_xp = user["xp"] + xp_earned
    new_level = new_xp // 100 + 1
    new_score = user["score"] + xp_earned

    conn.execute(
        "UPDATE users SET lesson_index = ?, xp = ?, level = ?, score = ? WHERE user_id = ?",
        (lesson_index, new_xp, new_level, new_score, user_id),
    )
    conn.commit()
    conn.close()


def mark_exercise_done(user_id, lesson_index, exercise_index, submitted_code="", output=""):
    conn = get_connection()
    conn.execute(
        """INSERT OR REPLACE INTO exercises (user_id, lesson_index, exercise_index, status, submitted_code, output, completed_at)
           VALUES (?, ?, ?, 'done', ?, ?, CURRENT_TIMESTAMP)""",
        (user_id, lesson_index, exercise_index, submitted_code, output),
    )
    conn.commit()
    conn.close()


def mark_exercise_failed(user_id, lesson_index, exercise_index, submitted_code="", output=""):
    conn = get_connection()
    conn.execute(
        """INSERT OR REPLACE INTO exercises (user_id, lesson_index, exercise_index, status, submitted_code, output, completed_at)
           VALUES (?, ?, ?, 'failed', ?, ?, CURRENT_TIMESTAMP)""",
        (user_id, lesson_index, exercise_index, submitted_code, output),
    )
    conn.commit()
    conn.close()


def get_user_exercises(user_id, lesson_index):
    conn = get_connection()
    cur = conn.execute(
        "SELECT * FROM exercises WHERE user_id = ? AND lesson_index = ? ORDER BY exercise_index",
        (user_id, lesson_index),
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def get_leaderboard(limit: int = 10):
    conn = get_connection()
    try:
        cur = conn.execute(
            """SELECT u.user_id, u.username, u.first_name, u.xp, u.level, u.streak, u.best_streak
               FROM users u ORDER BY u.xp DESC LIMIT ?""",
            (limit,),
        )
        rows = [dict(r) for r in cur.fetchall()]
    except sqlite3.OperationalError:
        # Старая схема базы — пересоздаём
        conn.close()
        init_db()
        return get_leaderboard(limit)
    conn.commit()
    conn.close()
    return rows


def reset_streak(user_id):
    conn = get_connection()
    conn.execute("UPDATE users SET streak = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
