
def get_choice():

    print('''
    Press 1 to add new venue
    Press 2 to add new item
    Press 3 to delete item
    Press 4 to show event venues
    press 5 to show items
    press 6 to add sold item
    press 7 to show sold items
    press 8 to check total items sold at a venue
    Press q to quit program
    ''')

    choice = input('Enter choice: ')

    return choice


def message(msg):
    '''Display a message to the user'''
    print(msg)
