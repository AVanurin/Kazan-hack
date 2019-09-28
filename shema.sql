DROP TABLE IF EXISTS appeals;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS statuses;
DROP TABLE IF EXISTS objects;
DROP VIEW IF EXISTS journal;

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
    login TEXT,
    name TEXT,
    job TEXT,
    location TEXT,
    chat_id INTEGER
);

CREATE TABLE objects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    object_type INTEGER,
    location TEXT
);

--Views

CREATE VIEW journal AS
    SELECT
        events.appeal_id, events.action, events.initiator, events.event_datetime,
        appeals.subject_id, appeals.content, appeals.category, appeals.assignee, appeals.solution, appeals.status,
        statuses.description
    FROM
        events
    LEFT JOIN appeals ON appeals.id = events.appeal_id
    LEFT JOIN statuses ON statuses.id = appeals.status;

--Enums

CREATE TABLE statuses
(
    id INTEGER PRIMARY KEY,
    description TEXT
);

INSERT INTO statuses VALUES (0, 'Зарегистрировано');
INSERT INTO statuses VALUES (1, 'Идет классификация');
INSERT INTO statuses VALUES (2, 'Идет начальное определение маршрута');
INSERT INTO statuses VALUES (3, 'Отдано на исполнение');
INSERT INTO statuses VALUES (4, 'Завершено');

