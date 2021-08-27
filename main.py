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
    return render_template("index.html", genres=["Fashion Jewellery", "Luxury Jewellery", "Gifts", "Normal Watches", "Luxury Watches"])



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
    # c = getcookie()
    itemid = request.args.get('itemid')
    name = request.args.get('name')

    itemdetails = database.db_getItemDetails(itemid)

    return render_template('description.html', name=name, itemdetails=itemdetails)


@app.route("/search_results/", methods=['GET', 'POST'])
def results():
    search = request.form['search']

    #movies = database.db_search(search)

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

    if loginsuccess:
        employeeid = database.db_getEmployeeID(username)
        set_user_cookie()

    return render_template('index.html', title="Index", username=username, loginsuccess=loginsuccess, cookie=c)


@app.route("/new_item", methods=['POST', 'GET'])
def new_item():
    user = get_user_session()

    stockid = request.form['stockid']
    name = request.form['name']
    itemtype = request.form['itemtype']
    description = request.form['description']
    imgurl = request.form['imgurl']
    buyprice = request.form['buyprice']
    sellprice = request.form['sellprice']
    discount = 0.0

    db_conn = database.db_insert_item(stockid, name, itemtype, description, imgurl, buyprice, sellprice, discount)
    if itemtype == "WATN" or itemtype == "WATL":
        clockwork = request.form['clockwork']
        calibre = request.form['calibre']
        casematerial = request.form['casematerial']
        caseshape = request.form['caseshape']
        casewidth = request.form['casewidth']
        casedepth = request.form['casedepth']
        glasstype = request.form['glasstype']
        dial = request.form['dial']
        dialcolour = request.form['dialcolour']
        bracelet = request.form['bracelet']
        clasp = request.form['clasp']
        features = request.form['features']
        batterycharge = request.form['batterycharge']
        service = request.form['service']
        diamondsnumber = request.form['diamondsnumber']
        diamondscarat = request.form['diamondscarat']
        diamondsquality = request.form['diamondsquality']
        numbercoloured = request.form['numbercoloured']
        colours = request.form['colours']

        database.db_insert_watch(db_conn, stockid, clockwork, calibre, casematerial, caseshape, casewidth, casedepth,
                                 glasstype, dial, dialcolour, bracelet, clasp, features, batterycharge, service,
                                 diamondsnumber,
                                 diamondscarat, diamondsquality, numbercoloured, colours)

    elif itemtype == "JWLL" or itemtype == "JWLF":
        # Basic jewellery details
        design = request.form['design']
        clasptype = request.form['clasptype']
        chainlength = request.form['chainlength']
        ringsize = request.form['ringsize']
        ringwidth = request.form['ringwidth']

        # Diamond details
        colour = request.form['colour']
        clarity = request.form['clarity']
        cut = request.form['cut']
        quality = request.form['quality']

        # Metal details
        material = request.form['material']
        materialgroup = request.form['materialgroup']
        alloy = request.form['alloy']
        unitweight = request.form['unitweight']

        database.db_insert_jewellery(db_conn, stockid, design, clasptype, chainlength, ringsize, ringwidth, colour,
                                     clarity, cut,
                                     quality, material, materialgroup, alloy, unitweight)

    else:

        articlegroup = request.form['articlegroup']
        articlekind = request.form['articlekind']
        brand = request.form['brand']
        productline = request.form['productline']
        collection = request.form['collection']

        database.db_insert_gift(db_conn, stockid, articlegroup, articlekind, brand, productline, collection)

    return render_template('productDesc.html', title="Product Description", user=user)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
