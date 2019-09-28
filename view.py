from flask import render_template
import db


def home_page():
    return render_template("index.html")


def render_all_events_page():
    events = db.get_journal_information()
    return render_template("journal.html", events=events)


def render_events_details(appeal_id):
    context = {}
    context['events'] = db.get_events_with_appeal_id(appeal_id)
    context['appeal'] = db.get_appeal_by_id(appeal_id)

    return render_template('event_details.html', data=context)


def all_tasks_page():
    task_list = []
    appeals = db.get_all_appeals()

    for appeal in appeals:
        temp = {}
        temp['id'] = appeal[0]
        temp['object_id'] = appeal[1]
        temp['category'] = ''
        temp['type'] = ''
        temp['status'] = 'Идет классификация'
        task_list.append(temp)

    #tasks = db.get_all_tasks()

    #for task in tasks:
        #pass

    return render_template("table.html", tasks=task_list)


def appeal_form():
    return render_template("form.html")