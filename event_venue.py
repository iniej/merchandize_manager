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
        add_sold_items()
    elif choice == '7':
        show_sold_list_items()
    elif choice == '8':
        total_items_sold_venues()
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
        cur.execute('''CREATE TABLE if NOT EXISTS items (item_id INTEGER PRIMARY KEY,
        venue_id INTEGER REFERENCES venue(venue_id), item_name TEXT)''')

def make_sold_items_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if NOT EXISTS sold_items (sold_item_id INTEGER PRIMARY KEY,\
         item_id INT REFERENCES items_table(item_id), item_name TEXT, item_price MONEY, sold_qty INT)''')


def add_new_venue():
    '''add a new venue'''
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
        cur.execute('INSERT INTO items VALUES (?,?,?)', (None, venue_id, item_name))


def add_sold_items():
    '''add sold item to the table'''
    item_id = input('Enter item_id ')
    item_name = input('Enter name of item: ')
    item_price = input('Enter price ')
    sold_qty = input('Enter quantity sold ')

    make_sold_items_table()

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()

        cur.execute('INSERT INTO sold_items VALUES (?,?,?,?,?)', (None, item_id, item_name, item_price, sold_qty))


def show_list_venues():
    ''' Display a list of all items'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        places = cur.execute('SELECT * FROM venue').fetchall()

    if len(places) == 0:
        print ('* No items *')
    else:
        for row in places:
            print(row)




def show_list_items():
    ''' Display a list of all items'''
    try:
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            places = cur.execute('SELECT * FROM items').fetchall()
    except Error as e:
        print(e)
    if len(places) == 0:
        print ('* No items *')
    else:
        for row in places:
            print(row)

def show_sold_list_items():
    ''' Display a list of all sold items'''
    try:
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            places = cur.execute('SELECT * FROM sold_items').fetchall()
    except Error as e:
        print(e)
    if len(places) == 0:
        print ('* No items *')
    else:
        for row in places:
            print(row)

def delete_item():
    ''''Delete items from the items table'''

    id = input('Enter item_id ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()

        delete_statement = ('DELETE FROM items WHERE item_id = ?')
        cur.execute(delete_statement, (id,))

def total_items_sold_venues():
    ''' Display item sold at a partiicular venue '''
    item = input('Enter the item ')

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        sqlite_statement = ('''SELECT venue_name, item_name, SUM(sold_qty) FROM sold_items JOIN items ON sold_items.item_id = items.item_id
                            JOIN venue ON venue.venue_id = items.venue_id WHERE sold_item.item_id = ?''')
        itemsSold = cur.execute(sqlite_statement, (item_id,)).fetchall()
        for i in itemsSold:
            print(i[2], i[1], ' were sold at ', i[0])




def main():


    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.get_choice()
        handle_choice(choice)




if __name__ == '__main__':
    main()
