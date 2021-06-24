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

@dispatch()
def db_getClients():
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from CLIENT_TABLE")
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
    

@dispatch(string)
def db_getClients(name):
    try:
        # Connect to Database
        db_conn = None
        db_conn = db_engine.connect()
        
        # Query database for users
        db_res = db_conn.execute("SELECT * from CLIENT_TABLE WHERE ")
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
    pass

@dispatch(string)
def db_getItemsWith(query):
    pass

def db_getClients():
    pass

def db_getClients():
    pass

def db_getClients():
    pass

def db_getTopVentas(anno):
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()


        db_resul = db_conn.execute("select * from getTopVentas(%s)", (anno,))
        db_resul = db_resul.fetchall()
        db_conn.close()

        return  list(db_resul)
    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '*******Something is broken on getTopVentas**********'
        print (error)
        return None

def db_register(Fname, Lname, age, address1,address2, city, state, country, region, zip, gender, email, phone, creditcard, creditcardtype, creditcardexp, username, password):
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select * from customers where username=%s", (username,))
        row = resul.fetchone()
        if row == None:
            if age == '':
                age=0

            else:
                int(age)
            id=1
            resul = db_conn.execute("select max(customerid) from customers")
            id += resul.fetchone()[0]
            income = random.randint(0,100)
            db_conn.execute("INSERT INTO customers(customerid, firstname, lastname, age, address1, address2,city, state, country, region, zip, gender, email, phone, creditcard,creditcardtype, creditcardexpiration, username, password, income)VALUES(%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, Fname, Lname, age,address1, address2, city, state, country, region, zip, gender, email, phone,creditcard, creditcardtype, creditcardexp, username, password,income,))
            print '***********Query register success***********'
            db_conn.close()
            return True
        else:
            print '***********Query register failed, username already exists***********'
            db_conn.close()
            return False

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '*******Something is broken on register**********'
        print (error)
        return False


def db_login(username, password):
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select password from customers where username=%s", (username,))
        row = resul.fetchone()
        if row != None:
            if row[0] == hashlib.md5(password).hexdigest():

                print '***********Query login success***********'
                db_conn.close()
                return True
            else:
                print '***********Query login failed, wrong password***********'
                db_conn.close()
                return False
        else:
            print '***********Query login failed, username doesnt exist***********'
            db_conn.close()
            return False
    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on login*****************'
        print (error)
        return False


def db_getDetails(movieid):
    try:

        movie = []

        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select price, description from imdb_movies natural join products where movieid=%s", (movieid,))
        movies=[]
        aux1=[]
        aux2=[]
        for x in resul:
            aux1.append(str(x[0]))
            aux2.append(x[1].encode('ascii', 'ignore'))
        movies.append(aux1)
        movies.append(aux2)
        resul = db_conn.execute("select actorname from (imdb_movies natural join imdb_actormovies) natural join imdb_actors where movieid=%s LIMIT 10", (movieid,))
        actors=[]
        for x in resul:
            actors.append(x[0].encode('ascii', 'ignore'))

        resul = db_conn.execute("select directorname from (imdb_movies natural join imdb_directormovies) natural join imdb_directors where movieid=%s", (movieid,))
        directors = []
        for x in resul:
            directors.append(x[0].encode('ascii', 'ignore'))

        resul = db_conn.execute("select genre from (imdb_movies natural join imdb_moviegenres) natural join imdb_genres where movieid=%s", (movieid,))
        genres = []
        for x in resul:
            genres.append(x[0].encode('ascii', 'ignore'))


        resul = db_conn.execute("select lang from (imdb_movies natural join imdb_movielanguages) natural join imdb_languages where movieid=%s", (movieid,))
        languages = []
        for x in resul:
            languages.append(x[0].encode('ascii', 'ignore'))

        db_conn.close()

        movie.append(list(movies))
        movie.append(list(actors))
        movie.append(list(directors))
        movie.append(list(genres))
        movie.append(list(languages))


        return movie

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on catalogue*****************'
        print (error)
        return None


def db_catalogue():
    try:

        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select movieid, movietitle from imdb_movies  LIMIT 50")
        resul = resul.fetchall()
        print '***********Query catalogue success***********'
        db_conn.close()

        return list(resul)

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on catalogue*****************'
        print (error)
        return None


def db_getCustomerid(username):
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select customerid from customers where username=%s", (username,))
        resul = resul.fetchone()[0]
        print '***********Query db_getCustomerid success***********'
        db_conn.close()

        return resul

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_getCustomerid*****************'
        print (error)
        return None

def db_getCustomerIncome(customerid):
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select income from customers where customerid=%s", (customerid,))
        resul = resul.fetchone()[0]
        print '***********Query db_getCustomerIncome success***********'
        db_conn.close()

        return resul

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_getCustomerIncome*****************'
        print (error)
        return None

def db_search(title, genre):
    try:

        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()
        title = '%'+title+'%'

        if title == "":
            if genre != "#":
                resul = db_conn.execute("select movieid, movietitle from (imdb_movies natural join imdb_moviegenres) natural join imdb_genres where genre = %s LIMIT 50", (genre,))
                resul = resul.fetchall()
            else:
                resul = db_catalogue()
        else:
            if genre != "#":
                resul = db_conn.execute("select movieid, movietitle from (imdb_movies natural join imdb_moviegenres) natural join imdb_genres where genre = %s and movietitle LIKE %s LIMIT 50", (genre,title,))
                resul = resul.fetchall()
            else:
                resul = db_conn.execute("select movieid, movietitle from (imdb_movies natural join imdb_moviegenres) natural join imdb_genres where movietitle LIKE %s LIMIT 50 ", (title,))
                resul = resul.fetchall()


        print '***********Query db_search success***********'
        db_conn.close()

        return list(resul)

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_search*****************'
        print (error)
        return None



def db_genres():
    try:
        # conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        resul = db_conn.execute("select * from imdb_genres")
        resul = resul.fetchall()
        print '***********Query genres success***********'
        db_conn.close()
        return list(resul)

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on genres*****************'
        print (error)
        return None

def db_addToCart(customerid, prodid):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        set = []

        result = db_conn.execute("SELECT orderid FROM orders WHERE customerid=%s AND status IS NULL", (customerid,))
        row = result.fetchone()
        # Aqui se comprueba el caso de que no exista un order para ese usuario
        if row == None:
            # Entonces se tiene que crear el carrito primero en orders
            db_conn.execute("INSERT INTO orders (orderid, orderdate, customerid, status) values((SELECT MAX(orderid)+1 FROM orders),current_date, %s, NULL)", (customerid,))
            # Luego se devuelve el orderid del nuevo carrito
            result = db_conn.execute("SELECT orderid FROM orders WHERE customerid=%s AND status IS NULL", (customerid,))
            row = result.fetchone()

            set.append(str(row[0]).encode('ascii', 'ignore'))
            set.append(str(prodid))

            # Y por fin, se ejecuta el insertar en carrito
            db_conn.execute("INSERT INTO orderdetail(orderid, prod_id)values(%s, %s)", (set,))

        # Aqui se comprueba el caso donde ya existe un carrito
        else:
            # Primero hay que comprobar que ese usuario no tiene ese producto ya
            resul = db_conn.execute("SELECT prod_id FROM orderdetail WHERE orderid=%s", (row,))
            item_exists = resul.fetchall()

            set.append(str(row[0]).encode('ascii', 'ignore'))
            set.append(str(prodid))

            # En el caso de que no haya nada en el carrito, lo inserta directamente
            if item_exists == None:
                db_conn.execute("INSERT INTO orderdetail (orderid, prod_id) values(%s, %s)", (set,))

            flag = 0

            # En el caso de anadir otro producto igual, se hace un update de la cantidad
            for x in item_exists:
                if x[0] == prodid:
                    db_conn.execute("UPDATE orderdetail SET quantity=quantity+1 WHERE orderid=%s AND prod_id=%s", (set,))
                    flag = 1
                    break

            # En el caso de que no lo tenga, se hace un insert igual que arriba
            if flag == 0:
                db_conn.execute("INSERT INTO orderdetail (orderid, prod_id) values(%s, %s)", (set,))

        print '***********Query addToCart success***********'
        db_conn.close()
        return

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on addToCart*****************'
        print (error)
        return

def db_removeFromCart(customerid, prodid):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        set = []

        # Aqui se coge la fila de la tabla orders del carrito del cliente
        result = db_conn.execute("SELECT orderid FROM orders WHERE customerid=%s AND status IS NULL", (customerid,))
        row = result.fetchone()

        # Aqui se coge todos los productos en el carrito
        resul = db_conn.execute("SELECT prod_id, quantity FROM orderdetail WHERE orderid=%s", (row,))
        item_exists = resul.fetchall()

        set.append(str(row[0]).encode('ascii', 'ignore'))
        set.append(str(prodid))

        # Para todos los productos, compara los id's con el id dado
        for x in item_exists:
            if x[0] == prodid:
                if x[1] > 1:
                    db_conn.execute("UPDATE orderdetail SET quantity=quantity-1 WHERE orderid=%s AND prod_id=%s", (set,))
                else:
                    db_conn.execute("DELETE FROM orderdetail WHERE orderid=%s AND prod_id=%s", (set,))
                break

        print '***********Query removeFromCart success***********'
        db_conn.close()
        return

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on removeFromCart*****************'
        print (error)
        return


def db_getCart(customerid):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        result = db_conn.execute("SELECT movieid, movietitle, price, prod_id, quantity FROM ((orders natural join orderdetail)natural join products)natural join imdb_movies WHERE customerid=%s and status is NULL", (customerid,))
        row = result.fetchall()

        print '***********Query db_getCart success***********'
        db_conn.close()
        return list(row)

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_getCart*****************'
        print (error)
        return None

def db_getProductId(movieid, price):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        result = db_conn.execute("SELECT prod_id FROM products WHERE movieid=%s AND price=%s", (movieid, str(price),))
        row = result.fetchone()[0]

        print '***********Query db_getProductId success***********'
        db_conn.close()
        return row

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_getProductId*****************'
        print (error)
        return None

def db_getMovie(movieid):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        result = db_conn.execute("SELECT movieid, movietitle FROM imdb_movies WHERE movieid=%s", (movieid,))
        row = result.fetchone()
        print '***********Query db_getMovie success***********'
        db_conn.close()
        return list(row)

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_getMovie*****************'
        print (error)

def db_geTotalAmount(customerid):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        result = db_conn.execute("SELECT totalamount FROM orders WHERE customerid=%s and status is NULL", (customerid,))
        row = result.fetchone()
        row = str(row[0])
        print '***********Query db_geTotalAmount success***********'
        db_conn.close()
        return row

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_geTotalAmount*****************'
        print (error)

def db_buy(customerid, income):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        db_conn.execute("UPDATE orders set status='Paid'  WHERE customerid=%s and status is NULL", (customerid,))
        db_conn.execute("UPDATE customers SET income=income-%s WHERE customerid=%s", (income, customerid,))
        print '***********Query db_geTotalAmount success***********'
        db_conn.close()
        return

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_geTotalAmount*****************'
        print (error)

def db_increaseIncome(customerid, income):
    try:
        db_conn = None
        db_conn = db_engine.connect()

        db_conn.execute("UPDATE customers set income=income+%s  WHERE customerid=%s", (income, customerid,))
        print '***********Query db_increaseIncome success***********'
        db_conn.close()
        return

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
        print '************Something is broken on db_increaseIncome*****************'
        print (error)
