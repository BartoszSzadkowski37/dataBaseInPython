# This file creates books db and manage it

# import module sqlite3
import sqlite3
import pyinputplus as pyip

# creating DB connection
con = sqlite3.connect('books.db')

# creating access to the columns by indexes and names
con.row_factory = sqlite3.Row

# creating cursor object
cur = con.cursor()

# CREATING TABLES
cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS clients(
        idClient INTEGER PRIMARY KEY ASC,
        name VARCHAR(250) NOT NULL,
        surname VARCHAR(250) NOT NULL,
        city VARCHAR(250) NOT NULL
        )''')

cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS books(
        idBook INTEGER PRIMARY KEY ASC,
        authorName VARCHAR(250) DEFAULT "",
        authorSurname VARCHAR(250) DEFAULT "",
        title VARCHAR(250) NOT NULL,
        price FLOAT NOT NULL
        )''')

cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS orders(
        idOrder INTEGER PRIMARY KEY ASC,
        idClient INTEGER NOT NULL,
        idBook INTEGER NOT NULL,
        data DATE NOT NULL,
        state VARCHAR(250) NOT NULL
        )''')

con.commit()

def printMenu():
    print('1. ADD NEW RECORDS')
    print('2. SHOW RECORDS')
    print('3. DELETE RECORDS')

# interface for adding new records
def addRecords():
    userInput = pyip.inputMenu(['clients', 'books', 'orders'])
    if userInput == 'clients':
        name = pyip.inputStr('name:')
        surname = pyip.inputStr('surname:')
        city = pyip.inputStr('city:')
        cur.execute('INSERT INTO clients VALUES(NULL, ?, ?, ?);', (name, surname, city))

    con.commit()

# interface for getting records from DB
def getRecords():
    userInput = pyip.inputMenu(['clients', 'books', 'orders'])
    if userInput == 'clients':
        cur.execute(
                '''
                SELECT * FROM clients
                ''')
        clients = cur.fetchall()
        for client in clients:
            print(client['idClient'], client['name'], client['surname'], client['city'])
        print()

printMenu()

userInput = pyip.inputChoice(['1', '2', '3'], 'Select number: ')

if userInput == '1':
    addRecords()

elif userInput == '2':
    getRecords()
