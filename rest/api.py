import json
from rest.register import register
from rest.info import get_info


def register_new_appeal_json(json_data):
    d = json.load(json_data)
    register(d)
    return "Ok"


def get_info_of_appeal(appeal_id):
    return get_info(appeal_id)