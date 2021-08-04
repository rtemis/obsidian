import string

from sqlalchemy import create_engine, func, exc
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
from multipledispatch import dispatch
import os
import hashlib
import random


# Configure database engine
db_engine = create_engine("postgresql://alumnodb:alumnodb@localhost/si1", echo=False)
db_meta = MetaData(bind=db_engine)


####################################################
#       EMPLOYEE DATABASE
####################################################
def db_create_sys_user(firstname, lastname, password, hiredate):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Insert into database
        db_conn.execute("INSERT INTO employee_table (firstname, lastname, password, hire_date) VALUES (%s, %s, %s, %s)",
                        (firstname, lastname, password, hiredate,))
        db_conn.close()

        return None

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: employee_table ******")
        print(error)
        return None


def db_get_sys_user(firstname, lastname, password):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Insert into database
        db_conn.execute("SELECT * FROM employee_table WHERE (firstname, lastname, password)=(%s, %s, %s)",
                        (firstname, lastname, password,))
        db_conn.close()

        return None

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: employee_table ******")
        print(error)
        return None


#################################################
#                CLIENT DATABASE
#################################################
@dispatch()
def db_getClients():
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from client_table")
        db_res = db_res.fetchall()
        db_conn.close()

        return list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print("****** Table error: client_table ******")
        print(error)
        
        return None
    

@dispatch(str)
def db_getClients(name):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from client_table WHERE first_name = (%s) OR last_name = (%s) OR client_id = (%s)", (name,))
        db_res = db_res.fetchall()
        db_conn.close()

        return list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print("****** Table error: client_table ******")
        print(error)

        return None


def db_getClientDetails(clientid):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Query database for users
        db_res = db_conn.execute(
            "SELECT * from client_table WHERE client_id = (%s)", (clientid,))
        db_res = db_res.fetchall()
        db_conn.close()

        return list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: client_table ******")
        print(error)

        return None


#################################################
#               ITEMS DATABASE
#################################################
@dispatch()
def db_getItems():
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from items_table")
        db_res = db_res.fetchall()
        db_conn.close()

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print("****** Table error: items_table ******")
        print(error)
        
        return None

@dispatch(str)
def db_getItems(query):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from items_table WHERE itemid=%s OR name=%s OR description", (query,))
        db_res = db_res.fetchall()
        db_conn.close()

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print ("****** Table error: items_table ******")
        print (error)
        
        return None


def db_search(query):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Query database for users
        db_res = db_conn.execute("SELECT * from items_table WHERE itemid=%s OR name=%s OR description")
        db_res = db_res.fetchall()
        db_conn.close()

        return list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: products_table ******")
        print(error)

        return None


def db_getItemDetails(itemid):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Query database for item
        db_res = db_conn.execute("SELECT * from items_table WHERE itemid=%s", itemid)
        db_res = db_res.fetchall()
        db_conn.close()

        return list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: item_table ******")
        print(error)

        return None


def db_insert_item(stockid, name, itemtype,	description, imgurl, buyprice, sellprice, discount):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Insert into database
        db_conn.execute("INSERT INTO items_table (stockid, name, itemtype,	description, imgurl, buyprice, sellprice, "
                        "discount) VALUES (%s, %s, %s, %s, %s, %2f, %2f, %2f)",
                        (stockid, name, itemtype,	description, imgurl, buyprice, sellprice, discount))

        if itemtype is "WATN" or itemtype is "WATL":
            insert_watch(db_conn)

        elif itemtype is "JWLL" or itemtype is "JWLF":
            insert_jewellery(db_conn)

        else:
            insert_gift(db_conn)

        db_conn.close()

        return None

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: items_table ******")
        print(error)
        return None

def insert_watch(db_conn):
    pass

def insert


def db_insert_watch(db_conn, stockid, clockwork, calibre, casematerial, caseshape, casewidth, casedepth, glasstype, dial, dialcolour, bracelet, clasp, features, batterycharge, service, diamondsnumber, diamondscarat, diamondsquality, numbercoloured, colours):
    # Insert into database
    db_conn.execute(
        "INSERT INTO watches_table (stockid, clockwork, calibre, casematerial, caseshape, casewidth, casedepth,"
        " glasstype, dial, dialcolour, bracelet, clasp, features, batterycharge, service, diamondsnumber, "
        "diamondscarat, diamondsquality, numbercoloured, colours) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %s, %d, %s)",
        (stockid, clockwork, calibre, casematerial, caseshape, casewidth, casedepth,
         glasstype, dial, dialcolour, bracelet, clasp, features, batterycharge, service, diamondsnumber,
         diamondscarat, diamondsquality, numbercoloured, colours,))