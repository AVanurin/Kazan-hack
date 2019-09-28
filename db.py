import sqlite3
from datetime import datetime


def _connect():
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    return conn, c

def test_db():
    conn, c = _connect()
    c.execute("SELECT * FROM appeals;")
    print(c.fetchall())
    c.execute("SELECT * FROM events;")
    print(c.fetchall())
    conn.close()

def init_dumb_data():
    conn, c = _connect()

    with open('dumb_bd.sql', 'r') as f:
        s = f.read()

    c.executescript(s)
    conn.commit()
    conn.close()


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


def change_appeal_status(appeal_id, new_status, action_description, initiator):
    conn, c = _connect()

    now_timestamp = str(datetime.now())

    s = f"""
    UPDATE appeals SET status={new_status} WHERE id=={appeal_id};
    INSERT INTO events (appeal_id, action, initiator, event_datetime) VALUES 
    ({appeal_id}, "{action_description}", "{str(initiator)}", "{now_timestamp}");
    """

    c.executescript(s)
    conn.commit()
    conn.close()


def get_journal_information():
    conn, c = _connect()
    c.execute("SELECT * FROM journal;")
    r = c.fetchall()
    conn.close()

    return r


def get_events_with_appeal_id(appeal_id):
    conn, c = _connect()
    c.execute(f"SELECT * FROM events WHERE appeal_id=={appeal_id}")
    r = c.fetchone()

    return r


def get_appeal_status_information(appeal_id):
    conn, c = _connect()
    c.execute(f"SELECT * FROM journal WHERE appeal_id=={appeal_id};")
    r = c.fetchall()
    conn.close()
    return r