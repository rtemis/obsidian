GBP = 1.0
EUR = 1.14
USD = 1.2

def set_exchange_rate(currency, newrate):
    global EUR
    global USD

    if (currency == 'EUR'):
        EUR = newrate
    elif (currency == 'USD'):
        USD = newrate
    else:
        print ("Error.")

def calculate_exchange(efrom, eto, quantity):
    if (efrom == 'EUR'):
        if (eto == 'GBP'):
            pass
        elif (eto == 'USD'):
            pass

    elif (efrom == 'GBP'):
        if (eto == 'EUR'):
            pass
        elif (eto == 'USD'):
            pass
    elif (efrom == 'USD'):
        if (eto == 'EUR'):
            pass
        elif (eto == 'GBP'):
            pass
    else:
        print ('Error')

