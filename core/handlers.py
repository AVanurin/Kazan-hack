import db
import json


def get_appeal_info_full(appeal_id):
    main_information = db.get_appeal_by_id(appeal_id)
    actions_information = db.get_appeal_status_information(appeal_id)
    return json.dumps(make_appeal_info_json(main_information, actions_information))


def make_appeal_info_json(appeal, actions):
    d = {}

    d['appeal_id'] = appeal[0]
    d['subject_id'] = appeal[1]
    d['text'] = appeal[2]
    d['start_date'] = appeal[3]
    d['category'] = appeal[4]
    d['assignee'] = appeal[5]

    actions_list = []
    for action in actions:
        tmp = {}
        tmp['action'] = action[1]
        tmp['initiator'] = action[2]
        tmp['datetime'] = action[3]
        tmp['assignee'] = action[7]
        tmp['status'] = action[10]
        actions_list.append(tmp)
    d['actions'] = actions_list

    print(d)
    print(json.dumps(d))

    return d