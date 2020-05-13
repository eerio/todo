own, simple and not secure todo app in Flask

usage:
$ EXPORT FLASK_APP=app.py
$ flask run

now access the app at localhost:5000
actually, the 'export flask_app=app.py' might be redundant,
because app.py is the default filename for a flask app, so
probably 'flask run' executed in the root dir of this
repo should be sufficient

lang: python3.7
dependencies: flask
