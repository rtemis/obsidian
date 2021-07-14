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

def db_create_sys_user(firstname, lastname, password):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Insert into database
        db_conn.execute("INSERT INTO employee_table (firstname, lastname, password) VALUES (%s, %s, %s)", (firstname, lastname, password,))
        db_conn.close()

        return None

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()

        print("****** Table error: employee_table ******")
        print(error)
        return None

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

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print ("****** Table error: client_table ******")
        print (error)
        
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

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print ("****** Table error: CLIENT_TABLE ******")
        print (error)
        
        return None

@dispatch()
def db_getItems():
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from products_table")
        db_res = db_res.fetchall()
        db_conn.close()

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print ("****** Table error: products_table ******")
        print (error)
        
        return None

@dispatch(str)
def db_getItems(query):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from products_table WHERE product_id=%s OR product_name=%s OR product_desc")
        db_res = db_res.fetchall()
        db_conn.close()

        return  list(db_res)

    except exc.SQLAlchemyError as error:
        # Connection error
        if db_conn is not None:
            db_conn.close()
        
        print ("****** Table error: client_table ******")
        print (error)
        
        return None


def db_search(query):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()

        # Query database for users
        db_res = db_conn.execute("SELECT * from products_table WHERE product_id=%s OR product_name=%s OR product_desc")
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

        print("****** Table error: client_table ******")
        print(error)

        return None

