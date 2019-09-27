from flask import render_template
import db


def home_page():
    return render_template("index.html")


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