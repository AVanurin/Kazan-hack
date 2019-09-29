import json
from rest.register import register
from rest.info import get_info


def register_new_appeal_json(json_data):
    d = json_data

    try:
        text = d['text']
        object_id = d['object_id']
        register(object_id, text)
        return "Ok"
    except:
        return "Error. Wrong json format"


def get_info_of_appeal(appeal_id):
    return get_info(appeal_id)

json_s = """
{
    "text": "Неработает двери у лифта. Разберитесь, что с этим может быть не так",
    "object_id": "12345"
}
"""


if __name__ == "__main__":
    register_new_appeal_json(json_s)