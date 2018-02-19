import sqlite3
import datetime
import ui
db_name = 'Event.db'


def handle_choice(choice):


    if choice == '1':
        add_new_venue()
    elif choice == '2':
        add_new_item()
    elif choice == '3':
        delete_item()
    elif choice == '4':
        show_list_venues()
    elif choice == '5':
        show_list_items()
    elif choice == '6':
        add_sold_item()
    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid number or enter q to quit ')


def make_venue_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS venue (venue_id INTEGER PRIMARY KEY,
        venue_name TEXT, venue_date date)''')


def make_items_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if NOT EXISTS items_table (item_id INTEGER PRIMARY KEY,
        venue_id INT REFERENCES venue(venue_id), item_name TEXT, item_price MONEY)''')

def make_sold_items_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if NOT EXISTS sold_items_table (item_id INT REFERENCES items_table(item_id),
        venue_id INT REFERENCES venue(venue_id), item_name TEXT, item_price MONEY, sold_qty INT)''')


def add_new_venue():
    # get new data, call method to add to DB
    venue_name = input('Enter name venue name: ')
    today = datetime.datetime.now()
    today = str(today.month)+'/'+str(today.day)+'/'+str(today.year)
    make_venue_table()
    
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('INSERT INTO venue VALUES (?, ?, ?)', (None, venue_name, venue_date))




def add_new_item():

    '''add merchandize to the items table'''
    item_name = input('Enter name name of item: ')
    item_price = input('Enter price ')

    venue_id = input('enter venue_id  ')
    make_items_table()

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute('INSERT INTO items_table VALUES (?,?,?,?)', (None, venue_id, item_name, item_price))


def add_sold_item():
    item_id = input('Enter item_id ')
    venue_id = input('Enter venue_id ')
    item_name = input('Enter name of item: ')
    item_price = input('Enter price ')
    sold_qty = input('Enter quantity sold ')


    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        # cur.execute('PRAGMA foreign_keys = ON')
        cur.execute('INSERT INTO sold_items_table VALUES (?,?,?,?,?)', (item_id, venue_id, item_name, item_price, sold_qty))


def show_list_venues():
    ''' Display a list of all items'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        places = cur.execute('SELECT * FROM venue').fetchall()
        # cur.execute('SELECT * FROM venue')
        # obj = cur.fetchall()
        # row_count = len(obj)
    if len(places) == 0:
        print ('* No items *')
    else:
        for p in places:
            print(p)

    # print ('venue_id     ',' venue_name      ','venue_date')
    # print ('----------------------------------------------')
    # while i < row_count:
    #         # print( places[i][0], '' *(16 - len(places[i])), places[i][1], '' *(16 - len(places[i][1])), places[i][2], '' *(16 - len(places[i][2])))
    #         print(obj[i][0], '' *(16 - len(obj[i][0])), obj[i][1], '' *(16 - len(obj[i][1])), obj[i][2], '' *(16 - len(obj[i][2])))



def show_list_items():
    ''' Display a list of all items'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        places = cur.execute('SELECT * FROM items_table').fetchall()
    if len(places) == 0:
        print ('* No items *')
    else:
        for p in places:
            print(p)

def delete_item():
    ''''Delete items from the items table'''

    item = input('Enter item_id ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        items = cur.execute('SELECT * FROM items_table').fetchall()
        # items = cur.execute('SELECT* FROM items_table WHERE item_name == item')
        # items_table.remove(item_id)


    for item_id in items:
        if item_id == item:
            # print(item_id)
            items.remove(item_id)
        else:
            print('item not found')


def main():


    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.get_choice()
        handle_choice(choice)


main()
