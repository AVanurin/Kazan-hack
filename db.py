import sqlite3


def _connect():
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    return conn, c


def init_db():
    conn, c = _connect()

    with open('shema.sql', 'r') as f:
        s = f.read()

    c.executescript(s)
    conn.commit()
    conn.close()


def add_new_appeal(subject_id, content, date):
    conn, c = _connect()
    s = f'INSERT INTO appeals (subject_id, content, start_date) VALUES ({subject_id}, "{content}", "{date}");'

    c.execute(s)
    conn.commit()
    new_entry_id = c.lastrowid
    conn.close()

    return new_entry_id


def get_appeal_by_id(_id: int):
    conn, c = _connect()

    s = f"SELECT * from appeals WHERE id={_id};"
    c.execute(s)
    appeal = c.fetchone()

    conn.close()
    return appeal


def get_all_appeals():
    conn, c = _connect()

    s = "SELECT * FROM appeals;"
    c.execute(s)
    result = c.fetchall()

    conn.close()
    return result


def get_all_tasks():
    conn, c = _connect()

    s = "SELECT * FROM tasks;"
    c.execute(s)

    result = c.fetchall()
    return result
