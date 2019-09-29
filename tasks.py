from Recognition.recognizer import get_classification
import db
from lxml import etree
from CAP.Notifications import CAPManager


def classify_appeal(text, task_id):
    change_status_of_appeal(task_id, 1, "Классификация", 'Webapp-form')
    category = get_classification(text=text)
    change_status_of_appeal(task_id, 2, "Опредление задачи", 'recognozer-Module')
    change_status_of_appeal(task_id, 3, "Опредление исполнителя", 'service-manager')
    change_category_of_appeal(task_id, category)
    #with open("test_log.txt", 'w') as f:
        #f.write(str(category))

    appeal = db.get_appeal_by_id(task_id)
    object_data = db.get_object_data(appeal[1])

    cm = CAPManager()
    cm._send_message(object_id=object_data[1], text=text, job="Gas worker", assignee_name="Петров А.В.", address=object_data[4], lattitude=object_data[2],
                     longitude=object_data[3], appeal_id=task_id)


def change_status_of_appeal(id, new_status, action_description, initiator):
    db.change_appeal_status(id, new_status, action_description, initiator)


def change_category_of_appeal(appeal_id, new_category):
    db.set_category(appeal_id, new_category)


def _get_class(classificaton):
    class_type = classificaton.get_class_type()
    return class_type


def assigne_worker():
    pass