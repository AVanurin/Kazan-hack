from flask import render_template
from flask import request
from datetime import datetime
import handlers


def render_form():
    return render_template("form.html")


def take_form_date():
    object_id = request.form.get('object_id')
    text = request.form.get('appeal_text')

    if object_id and text:
        r = handlers._register_new_appeal(subject_id=object_id, text=text, date=str(datetime.now()))
        return r
    else:
        return "Error"