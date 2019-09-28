INSERT INTO appeals (subject_id, content, start_date, category, assignee, solution, status) VALUES
            (
              12, "Моя жалоба на вас", "20.10.2019", "12.2", "Вася", Null, 3
            );

INSERT INTO appeals (subject_id, content, start_date, category, assignee, solution, status) VALUES
            (
              432, "Просто жалуюсь", "20.10.2019", "14.2", "Дима", Null, 2
            );

INSERT INTO appeals (subject_id, content, start_date, category, assignee, solution, status) VALUES
            (
              432, "Ну вот зачем", "20.10.2019", "17.2", "Олег", Null, 1
            );

INSERT INTO appeals (subject_id, content, start_date, status) VALUES
            (
              100, "Просто жалуюсь", "20.10.2019", 1
            );

INSERT INTO events (appeal_id, action, initiator, event_datetime) VALUES
    (
     1, "Записали", 'веб-сервис', "18.09.2019 14:20"
    );

INSERT INTO events (appeal_id, action, initiator, event_datetime) VALUES
    (
     1, "Обработали", 'компьютерные технологии', "18.09.2019 14:25"
    );

INSERT INTO events (appeal_id, action, initiator, event_datetime) VALUES
    (
     1, "Распределили", 'УК', "18.09.2019 14:35"
    );
