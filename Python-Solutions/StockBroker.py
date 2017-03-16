'''Clients place orders to a stockbroker as strings. The order can be simple or multiple.

Type of a simple order: Quote /space/ Quantity /space/ Price /space/ Status

where Quote is formed of non-whitespace character, Quantity is an int, Price a double (with mandatory decimal point "." ), Status is represented by the letter B (buy) or the letter S (sell).

Example:

"GOOG 300 542.0 B"

A multiple order is the concatenation of simple orders with a comma between each.

Example:

"ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"

To ease the stockbroker your task is to produce a string of type

"Buy: b Sell: s" where b and s are 'double' formatted with no decimal (rounded to integers), b representing the total price of bought stocks and s the total price of sold stocks.

Example:

"Buy: 294990 Sell: 0"

Unfortunately sometimes clients make mistakes. When you find mistakes in orders, you must pinpoint these badly formed orders and produce a string of type:

"Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"

where nb is the number of badly formed simple orders, b representing the total price of bought stocks with correct simple order and s the total price of sold stocks with correct simple order.

Examples:

"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"

"Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;"

Note: Due to Codewars whitespace differences will not always show up in test results.'''



def balance_statement(lst):
    if(len(lst) == 0):
        return "Buy: 0 Sell: 0"
    str1 = lst.split(',')
    buy = 0
    sell = 0
    bad = []
    for s in str1:
        stock = s.strip().split(' ')
        if len(stock) != 4:
            bad.append(stock)
        elif(stock[2].isdigit() == True):
            bad.append(stock)
        elif(stock[1].isdigit() == False):
            bad.append(stock)
        elif(stock[3] == 'B' or stock[3] =='S'):
            if stock[3] == 'B':
                buy += float(stock[1]) * float(stock[2])
            elif stock[3] == 'S':
                sell += float(stock[1]) * float(stock[2])
        else:
            bad.append(stock)
    
    bad_s = ''
    length = len(bad)
    l = str(length)
    if(length > 0):
        for b in bad:
            bad_s += ' '.join(b) + ' ;'
    if bad_s == '':
        return "Buy: " + str(int(round(buy))) + " Sell: " + str(int(round(sell)))
    else:
        return "Buy: " + str(int(round(buy))) + " Sell: " + str(int(round(sell))) + "; Badly formed " + l + ": " + bad_s;




'''def balance_statement(lst):
    bad_formed, prices = [], {'B':0, 'S':0}
    for order in filter(None, lst.split(', ')):
        if not re.match('\S+ \d+ \d*\.\d+ (B|S)', order):
            bad_formed.append(order + ' ;')
        else:
            _, quantity, price, status = order.split()
            prices[status] += int(quantity) * float(price)
    ret = "Buy: %.0f Sell: %.0f" % (prices['B'], prices['S'])
    if bad_formed:
        ret += "; Badly formed %d: %s" % (len(bad_formed), ''.join(bad_formed))
    return ret'''