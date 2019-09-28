import db
import requests
import json
from datetime import datetime
from taskmanager import TaskManager


taskmanager = TaskManager()


def register_new_appeal_json(json):
    subject_id = json["subject_id"]
    text_of_appeal = json["text"]
    start_date = datetime.now()

    _register_new_appeal(subject_id=subject_id, text=text_of_appeal, date=start_date)


def get_appeal_information_json(appeal_id):
    appeal = db.get_appeal_by_id(appeal_id)

    d = {
        "appeal_id": appeal[0]
    }


def _register_new_appeal(subject_id, text, date):
    new_task = db.add_new_appeal(subject_id, text, date)
    taskmanager.start_initial_analyze(text, new_task)
    if new_task != None:
        print(new_task)
        return new_task


def read_auidio():
    pass