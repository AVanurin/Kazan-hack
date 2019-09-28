from flask import Flask
from flask import request
from flask import render_template
from datetime import date
import views.static as static_view
import views.journal as journal_view
import view
import db
import handlers
from rest import api


#db.init_db()
#db.init_dumb_data()
#db.test_db()
app = Flask(__name__)


@app.route('/')
def index():
    return static_view.home_page()


@app.route('/tasks')
def tasks():
    return view.all_tasks_page()


@app.route('/form', methods=['POST'])
def another_name():
    object_id = request.form.get('object_id')
    text = request.form.get('appeal_text')

    r = handlers._register_new_appeal(subject_id=object_id, text=text, date=str(date.today()))
    appeal_id = str(r)
    return render_template('result.html', task=appeal_id)


@app.route('/form', methods=['GET'])
def render_form():
    return view.appeal_form()


@app.route('/events')
def render_journal_all():
    return journal_view.render_all_events_page()


@app.route('/rest/event/<event_id>')
def response_with_event_data(event_id):
    response = api.get_info(event_id)
    return str(response)


if __name__ == '__main__':
    app.run()
