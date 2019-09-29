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
    job TEXT,
    name TEXT,
    object_id INTEGER
);

CREATE TABLE objects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    lattituide REAL,
    longitude REAL,
    address TEXT
);


CREATE TABLE statuses
(
    id INTEGER PRIMARY KEY,
    description TEXT
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

INSERT INTO statuses VALUES (0, 'Зарегистрировано');
INSERT INTO statuses VALUES (1, 'Идет классификация');
INSERT INTO statuses VALUES (2, 'Идет начальное определение маршрута');
INSERT INTO statuses VALUES (3, 'Отдано на исполнение');
INSERT INTO statuses VALUES (4, 'Завершено');

INSERT INTO objects VALUES (12345, 'домохозяйство Пролетарский проспект, 20', 59.999181, 30.144061, "СПб,Пролетарский проспект, 20");
INSERT INTO objects VALUES (12347, 'домохозяйство Хвойная улица, 27', 60.000507, 30.143406, "СПб,Хвойная улица, 27");
INSERT INTO objects VALUES (12346, 'домохозяйство Пролетарский проспект, 26', 59.999206, 30.142261, "СПб,Пролетарский проспект, 26");
INSERT INTO objects VALUES (12348, 'территория Ольгино, Санкт-Петербург, Россия, Садовая улица, 46', 59.998282, 30.134295, "территория Ольгино, Санкт-Петербург, Россия, Садовая улица, 46");

INSERT INTO users (job, name, object_id) VALUES ('Plumber', "Сидренко О.М.", 12345);
INSERT INTO users (job, name, object_id) VALUES ('Plumber', "Петров А.В.", 12347);
INSERT INTO users (job, name, object_id) VALUES ('Plumber', "Колмак Т.И.", 12346);
INSERT INTO users (job, name, object_id) VALUES ('Plumber', "Антропов С.С.", 12348);