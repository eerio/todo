from flask import Flask
from flask import render_template, request

app = Flask(__name__)

things = ['posprzatac', 'pogotowac', 'odrobic zadanie']

@app.route('/', methods=['GET', 'POST'])
def hello():
    global things

    if request.method == 'POST':
        todo = request.form.get('todo')
        if todo:
            things.append(todo)

        deleted = 0
        for i in range(1, len(things) + 1):
            is_to_del = request.form.get(str(i)) is not None
            if is_to_del:
                things.pop(i - 1 - deleted)
                deleted += 1

    return render_template('index.html', things=things)

