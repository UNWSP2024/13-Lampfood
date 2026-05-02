#Elliott Morris, 4/29/2026, Accessing Cities.py

import sqlite3

def main():
    try:
        #Connect to the database
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(f'Error while connecting to database: {e}')
        return

    while True: #Keep the program running until the user quits
        display_menu()
        choice = get_choice()

        #Grab correct function based on choice
        if choice == 1:
            display_population_asc(cur)
        elif choice == 2:
            display_population_desc(cur)
        elif choice == 3:
            display_by_name(cur)
        elif choice == 4:
            display_total_population(cur)
        elif choice == 5:
            display_average_population(cur)
        elif choice == 6:
            display_highest_population(cur)
        elif choice == 7:
            display_lowest_population(cur)
        elif choice == 8:
            break

    #Close the Connection
    conn.close()

#display the menu options
def display_menu():
    print('\nCities Database Menu')
    print('1. Display cities sorted by population (ascending)')
    print('2. Display cities sorted by population (descending)')
    print('3. Display cities sorted by name')
    print('4. Display total population of all cities')
    print('5. Display average population of all cities')
    print('6. Display city with the highest population')
    print('7. Display city with the lowest population')
    print('8. Exit')

#get and validate user input
def get_choice():
    while True:
        user_input = input('Enter your choice (1-8): ').strip()

        if not user_input:
            print('Error: input cannot be blank.')
            continue

        if not user_input.isdigit():
            print('Error: please enter a whole number from 1 to 8.')
            continue

        choice = int(user_input)

        if choice < 1 or choice > 8:
            print('Error: choice must be between 1 and 8.')
            continue

        return choice

#makes the user hit enter to continue
def pause():
    input('\nPress Enter to return to the menu...')

def display_population_asc(cur):
    try:
        cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population ASC')
        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:20}{row[1]:,.0f}')

    except sqlite3.Error as e:
        print(f'Database Error: {e}')

    pause()

def display_population_desc(cur):
    try:
        cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population DESC')
        results = cur.fetchall()

        print('\nCities by Population (Descending)')
        for row in results:
            print(f'{row[0]:20}{row[1]:,.0f}')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

def display_by_name(cur):
    try:
        cur.execute('SELECT CityName, Population FROM Cities ORDER BY CityName ASC')
        results = cur.fetchall()

        print('\nCities by Population (Descending)')
        for row in results:
            print(f'{row[0]:20}{row[1]:,.0f}')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

def display_total_population(cur):
    try:
        cur.execute('SELECT SUM(Population) FROM Cities')
        result = cur.fetchone()

        print(f'\nTotal Population: {result[0]:,.0f}')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

def display_average_population(cur):
    try:
        cur.execute('SELECT AVG(Population) FROM Cities')
        result = cur.fetchone()

        print(f'\nAverage Population: {result[0]:,.0f}')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

def display_highest_population(cur):
    try:
        cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1')
        result = cur.fetchone()

        print(f'\nHighest Population: {result[0]} ({result[1]:,.0f})')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

def display_lowest_population(cur):
    try:
        cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1')
        result = cur.fetchone()

        print(f'\nLowest Population: {result[0]} ({result[1]:,.0f})')

    except sqlite3.Error as e:
        print(f'Error while accessing database: {e}')

    pause()

if __name__ == "__main__":
    main()