from http import cookies as Cookie

vacio = False
buysuccess = 0
cookiexists = False
anno = 0
user = False


# Create new user
def setusername(firstname, lastname, customerid):
    global user
    user = True
    global session
    session['username'] = username
    session['customerid'] = customerid
    global cookie
    cookie = Cookie.SimpleCookie()
    cookie['user'] = username
    global cookiexists
    cookiexists = True


def getcookie():
    if cookiexists == True:
        return str(cookie['user'].value)
    else:
        a = ""
        return a


def getcustomerid():
    return session.get('customerid')


def getusername():
    return session.get('username')


def getuser():
    global user
    return user
