import flask
import render_template

app = flask

flask(__name__)

jobs = render_template('index.html')

jobs.route(/)
