import sqlite3
import atexit
from datetime import datetime

from flask import Flask
from flask import render_template, request
from flask import g

DB_FILENAME = 'todo.db'
tb_name = 'todo'
desc = 'description'
date = 'date'

app = Flask(__name__)


def query(s):
    return s.format(tb_name=tb_name, desc=desc, date=date)


create_query = query(
    """
    CREATE TABLE IF NOT EXISTS {tb_name} (
        {desc} text,
        {date} text
        );
    """
    )

select_query = query(
    """
    SELECT * FROM {tb_name};
    """
    )

delete_query = query("DELETE FROM {tb_name};")

insert_query = query(
    """
    INSERT INTO {tb_name} ({desc}, {date})
    VALUES (?, ?);
    """
    )


# startup
con = sqlite3.connect(DB_FILENAME)

with con:
    cur = con.cursor()
    cur.execute(create_query)
    cur.execute(select_query)
    records = cur.fetchall()
    things = records

print(repr(things))

def teardown():
    with con:
        cur = con.cursor()
        cur.execute(delete_query)
        for rec in things:
            cur.execute(insert_query, rec)

atexit.register(teardown)

form = '%A, %d. %B %Y %I:%M%p'

@app.route('/', methods=['GET', 'POST'])
def hello():
    global things

    if request.method == 'POST':
        todo = request.form.get('todo')
        if todo:
            things.append((todo, datetime.now().strftime(form)))

        deleted = 0
        for i in range(1, len(things) + 1):
            is_to_del = request.form.get(str(i)) is not None
            if is_to_del:
                things.pop(i - 1 - deleted)
                deleted += 1
    return render_template('index.html', things=things)

