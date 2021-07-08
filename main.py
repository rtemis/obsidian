import os
import sys

from flask import Flask, render_template
from http import cookies

app = Flask(__name__)

# Setup sessions
try:
    from flask_session import Session
    this_dir = os.path.dirname(os.path.abspath(__file__))
    SESSION_FILE_DIR = this_dir + '/flask_session'
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_NAME = 'flasksessionid'
    app.config.from_object(__name__)
    Session(app)
    print >>sys.stderr, "Using Flask-Session sessions in server file"
except ImportError as e:
    print >>sys.stderr, "Flask-Session not available, using cookies"


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)