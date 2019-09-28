from Recognition.recognizer import get_classification
import db


def classify_appeal(text, task_id):
    change_status_of_appeal(task_id, 1, "Классификация", 'recognozer-Module')
    classification = get_classification(text=text)
    change_status_of_appeal(task_id, 2, "Опредление задачи", 'recognozer-Module')
    with open("test_log.txt", 'w') as f:
        f.write(str(classification))


def change_status_of_appeal(id, new_status, action_description, initiator):
    db.change_appeal_status(id, new_status, action_description, initiator)