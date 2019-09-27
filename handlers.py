import db


def register_new_appeal_json(json):
    text_of_appeal = json["???"]


def _register_new_appeal(subject_id, text, date):
    new_task = db.add_new_appeal(subject_id, text, date)
    if new_task != None:
        print(new_task)
        return new_task