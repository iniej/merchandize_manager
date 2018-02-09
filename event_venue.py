import sqlite3
import datetime
import ui
db_name = 'Event.db'


def handle_choice(choice):


    if choice == '1':
        add_new()
    elif choice == '2':
        show_list()

    elif choice == '6':
        show_list_items()
    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid number or enter q to quit ')



def add_new():
    # get new data, call method to add to DB
    venue_name = input('Enter name venue name: ')
    today = datetime.datetime.now()
    make_table()
    # add_to_db(venue_name, today)


    item_name = input('Enter name name of item: ')
    item_price = input('Enter price ')
    sold_qty = input('Enter quantity sold ')
    make_items_table()
    # add_to_db(venue_name, today, item_name, item_price, sold_qty)

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()

        cur.execute('INSERT INTO venue VALUES (?,?,?)', (None, venue_name, today))
        venue_id = cur.execute('SELECT venue_id FROM venue WHERE venue_name = ?',(venue_name,)).fetchone()
        venue_id = int(venue_id[0])
        cur.execute('INSERT INTO items_table VALUES (?,?,?,?,?)', (None, venue_id, item_name, item_price, sold_qty))

# def add_to_db(place_name, venue_date, item_name, item_price, sold_qty):

# def add_new_item():
#     # get new data, call method to add to DB
#     item_name = input('Enter name: ')
#     item_price = input('Enter price')
#     sold_qty = input('Enter quantity sold')
#     # today = datetime.datetime.now()
#     make_table_item()
#     add_to_db(item_name, item_price, sold_qty)


# def add_to_db(venue_name, venue_date):
#
#     with sqlite3.connect(db_name) as db:
#         cur = db.cursor()
#         cur.execute('INSERT INTO venue VALUES (?,?,?)', (None, venue_name, venue_date ))


def make_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS venue (venue_id INTEGER PRIMARY KEY, venue_name TEXT, venue_date DATETIME)')


def make_items_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if NOT EXISTS items_table (itmeid INTEGER PRIMARY KEY,
        venueid INT REFERENCES venue(venue_id), item_name TEXT, item_price MONEY, sold_qty INT)''')


def show_list():
    ''' Display a list of all items'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        places = cur.execute('SELECT * FROM venue').fetchall()
    if len(places) == 0:
        print ('* No items *')
    else:
        for p in places:
            print(p)

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



def main():


    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.get_choice()
        handle_choice(choice)


main()
