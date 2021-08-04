import os
import sys

from flask import Flask, render_template, url_for, request, redirect, session
import unicodedata
from sessions import *

import DatabaseManagement.dbConn as database

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
    print(sys.stderr, "Using Flask-Session sessions in server file")
except ImportError as e:
    print(sys.stderr, "Flask-Session not available, using cookies")


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sales")
def show_sales():
    return render_template("sales.html")

@app.route("/new_client")
def create_new_client():
    return render_template("new_client.html")

@app.route("/all_clients")
def show_all_clients():
    return render_template("all_clients.html")

@app.route("/item_lookup", methods=['GET', 'POST'])
def item_lookup():
    return render_template("item_lookup.html")

@app.route("/description/", methods=['GET', 'POST'])
def description():
    #c = getcookie()
    itemid = request.args.get('itemid')
    name = request.args.get('name')

    itemdetails = database.db_getItemDetails(itemid)

    return render_template('description.html', name=name, itemdetails=itemdetails)



@app.route("/search_results/", methods=['GET','POST'])
def results():
    search = request.form['search']

    movies = database.db_search(search)

    return render_template("search_results.html", search=search)

@app.route("/checkout")
def cart():
    pass


@app.route("/~", methods=['POST', 'GET'])
def user():
    c = get_cookie()
    username = request.form['user']
    password = request.form['password']

    loginsuccess = database.db_login(username, password)

    if loginsuccess == True:
        employeeid = database.db_getEmployeeID(username)
        set_user_cookie()

    return render_template('index.html', title="Index", username=username, loginsuccess = loginsuccess, cookie=c)

@app.route("/new_item", methods=['POST', 'GET'])
def new_item():
    c = get_cookie()




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)