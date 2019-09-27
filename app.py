from flask import Flask
from flask import request
from datetime import date
import view
import db
import handlers

db.init_db()
app = Flask(__name__)


@app.route('/')
def index():
    return view.home_page()


@app.route('/tasks')
def tasks():
    return view.all_tasks_page()


@app.route('/form', methods=['POST'])
def another_name():
    print("fired!")
    object_id = request.form.get('object_id')
    text = request.form.get('appeal_text')

    r = handlers._register_new_appeal(subject_id=object_id, text=text, date=str(date.today()))
    return str(r)


@app.route('/form', methods=['GET'])
def render_form():
    return view.appeal_form()


if __name__ == '__main__':
    app.run()
