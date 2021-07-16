from http import cookies as Cookie

cookieexists = False
user = False

##############################
#       Cookie values        #
##############################

# Create new user session
def set_user_cookie(firstname, lastname, employeeid):
    global user
    user = True
    global session
    session['user'] = firstname + ' ' + lastname
    session['employeeid'] = employeeid
    global cookie
    cookie = Cookie.SimpleCookie()
    cookie['user'] = firstname + ' ' + lastname
    global cookieexists
    cookieexists = True


# Get current cookie user value
def get_cookie():
    if cookieexists == True:
        user = str(cookie['user'].value)
    else:
        user = ""
    return user

##############################
#       Employee values      #
##############################

# Get Employee ID of current user
def get_employeeid():
    return session.get('employeeid')


# Get name of user in session
def get_user_name():
    return session.get('user')


# Get cookie value
def get_user_session():
    global user
    return user


def clear_cookie():
    global cookieexists
    global cookie

    if cookieexists:
        cookie = None
        cookieexists = False


###############################
#       Cart functions        #
###############################

# Create the empty cart value for the seller
def set_cart():
    global empty
    empty = True
    global session
    session['cart'] = []


# Add the new item to the cart
def add_cart(itemid, stockid):
    global session
    # Create item locator
    item = {"itemid": itemid, "stockid": stockid}
    # Add item to cart
    session['cart'].append(item)


# Remove an item from the cart
def del_cart(itemid, stockid):
    global session
    # Create the item locator
    item = {"itemid": itemid, "stockid": stockid}
    # Remove item from cart
    session['cart'].remove(item)


# Create a new cart
def clean_cart():
    global session
    session.pop('cart')
    set_cart()


# Get the current cart
def get_cart():
    return session.get('cart')

