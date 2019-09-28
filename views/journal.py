from flask import render_template
import db


def render_all_events_page():
    events = db.get_journal_information()
    print(events)
    context = make_events_context(events)
    return render_template("eventslist.html", events=context)


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


def make_event_details_context(events, appeal):
    context = []
    context['id'] = appeal[0]
    return context