DROP TABLE IF EXISTS appeals;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

CREATE TABLE appeals
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id integer,
    content    TEXT,
    start_date TEXT,
    category   TEXT,
    assignee   INTEGER,
    solution   TEXT,
    status INTEGER
);

CREATE TABLE events
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appeal_id INTEGER,
    action TEXT,
    initiator TEXT,
    event_datetime TEXT
);

CREATE TABLE users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job TEXT,
    location TEXT
);