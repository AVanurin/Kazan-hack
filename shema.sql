DROP TABLE IF EXISTS appeals;
DROP TABLE IF EXISTS tasks;

CREATE TABLE appeals
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id integer,
    content    TEXT,
    start_date TEXT,
    category   TEXT,
    assignee   INTEGER,
    solution   TEXT

);

CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT);