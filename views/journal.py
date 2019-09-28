from flask import render_template
import db


def render_all_events_page():
    events = db.get_journal_information()
    context = make_events_context(events)
    return render_template("eventslist.html", events=context)


def render_event(appeal_id):
    main_information = db.get_appeal_by_id(appeal_id)
    actions_information = db.get_appeal_status_information(appeal_id)
    context = make_event_details_context(main_information, actions_information)
    print(context)
    return render_template("anketa.html", context=context)


def render_event_details(appeal_id):
    context = {}
    context['events'] = db.get_events_with_appeal_id(appeal_id)
    context['appeal'] = db.get_appeal_by_id(appeal_id)

    return render_template('event_details.html', data=context)


def make_events_context(events_journal):
    context = []
    for event in events_journal:
        temp = {}
        temp['id'] = event[0]
        temp['object_id'] = event[4]
        temp['action'] = event[1]
        temp['category'] = event[6]
        temp['status'] = event[9]

        context.append(temp)
    return context


def make_event_details_context(appeal, actions):
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

    return d