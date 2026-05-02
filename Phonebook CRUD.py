#Elliott Morris, 4/29/2026, Phonebook CRUD.py

import sqlite3

def main():
    try:
        #Connect to the database
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(f'Error while connecting to database: {e}')
        return

    while True: #Keep the program running until the user quits
        display_menu()
        choice = get_choice()

        #Grab correct function based on choice
        if choice == 1:
            add_entry(conn, cur)
        elif choice == 2:
            look_up_number(cur)
        elif choice == 3:
            update_number(conn, cur)
        elif choice == 4:
            delete_entry(conn, cur)
        elif choice == 5:
            break

    #Close the connection
    conn.close()

#display the menu options
def display_menu():
    print('\nPhonebook Menu')
    print('1. Add a new entry')
    print('2. Look up a phone number')
    print('3. Change a phone number')
    print('4. Delete an entry')
    print('5. Exit')

#get and validate user input
def get_choice():
    while True:
        user_input = input('Enter your choice (1-5): ').strip()

        if not user_input:
            print('Error: input cannot be blank.')
            continue

        if not user_input.isdigit():
            print('Error: please enter a whole number from 1 to 5.')
            continue

        choice = int(user_input)

        if choice < 1 or choice > 5:
            print('Error: choice must be between 1 and 5.')
            continue

        return choice

#makes the user hit enter to continue
def pause():
    input('\nPress Enter to return to the menu...')

def add_entry(conn, cur):
    name = input('Enter name: ').strip()
    phone = input('Enter phone number: ').strip()

    if not name or not phone:
        print('Error: name and phone number cannot be blank.')
        pause()
        return

    try:
        cur.execute('INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)', (name, phone))
        conn.commit()
        print(f'\n{name} was added successfully.')

    except sqlite3.Error as e:
        print(f'Database Error: {e}')

    pause()

def look_up_number(cur):
    name = input('Enter name to look up: ').strip()

    if not name:
        print('Error: name cannot be blank.')
        pause()
        return

    try:
        cur.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
        result = cur.fetchone()

        if result:
            print(f'\n{name}\'s phone number is {result[0]}')
        else:
            print(f'\n{name} was not found.')

    except sqlite3.Error as e:
        print(f'Database Error: {e}')

    pause()

def update_number(conn, cur):
    name = input('Enter name to update: ').strip()

    if not name:
        print('Error: name cannot be blank.')
        pause()
        return

    try:
        cur.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
        result = cur.fetchone()

        if result:
            new_number = input('Enter new phone number: ').strip()

            if not new_number:
                print('Error: phone number cannot be blank.')
            else:
                cur.execute('UPDATE Entries SET PhoneNumber = ? WHERE Name = ?', (new_number, name))
                conn.commit()
                print(f'\n{name}\'s phone number was updated.')
        else:
            print(f'\n{name} was not found.')

    except sqlite3.Error as e:
        print(f'Database Error: {e}')

    pause()

def delete_entry(conn, cur):
    name = input('Enter name to delete: ').strip()

    if not name:
        print('Error: name cannot be blank.')
        pause()
        return

    try:
        cur.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
        result = cur.fetchone()

        if result:
            cur.execute('DELETE FROM Entries WHERE Name = ?', (name,))
            conn.commit()
            print(f'\n{name} was deleted successfully.')
        else:
            print(f'\n{name} was not found.')

    except sqlite3.Error as e:
        print(f'Database Error: {e}')

    pause()

if __name__ == "__main__":
    main()