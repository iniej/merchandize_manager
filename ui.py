
def get_choice():

    print('''
    Press 1 to add new record
    Press 2 to show event venue records
    Press 3 to delete record
    Press 4 to update record
    press 5 to search record
    press 6 to show items records
    Press q to quit program
    ''')

    choice = input('Enter choice: ') 

    return choice

def message(msg):
    '''Display a message to the user'''
    print(msg)
