# this file exist for figured out, how DB in Python works

import sqlite3

# creating connection with DB on the disk 
con = sqlite3.connect('test.db')

# access to column by indexes and names
con.row_factory = sqlite3.Row

# creating cursor object
cur = con.cursor()

# creating tables
cur.execute('DROP TABLE IF EXISTS myClass;')

cur.execute('''
        CREATE TABLE IF NOT EXISTS myClass (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT \'\'
        )''')

cur.executescript('''
        DROP TABLE IF EXISTS uczen;
        CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        myClass_id INTEGER NOT NULL,
        FOREIGN KEY(myClass_id) REFERENCES myClass(id)
        )''')


# adding record
cur.execute('INSERT INTO myClass VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
cur.execute('INSERT INTO myClass VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

# we perform SQL query which take ID 1A class from myClass table
cur.execute('SELECT id FROM myClass WHERE nazwa = ?', ('1A',)) # -!! remember about comma when you put only single argument, with comma you create 1-element tuple
# cur.fetchone() return current table row, we can specify by [value] exact field from the row ex. cur.fetchone()[1]
klasa_id = list(cur.fetchone())
# "uczniowie" tuple include tuple with students data
uczniowie = (
        (None, 'Tomasz', 'Nowak', 1),
        (None, 'Jan', 'Kos', 2),
        (None, 'Piotr', 'Kowalski', 1)
        )

# adding multiple records
cur.executemany('INSERT INTO uczen VALUES(?,?,?,?)', uczniowie)

# commit in DB
con.commit()

# GETTING DATA FROM DB
def readData():
    # function get and print dates from DB
    cur.execute(
            '''
            SELECT uczen.id, imie, nazwisko, nazwa, profil FROM uczen, myClass 
            WHERE uczen.myClass_id=myClass.id
            ''')
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'], uczen['profil'])
    print()
readData()

# MODIFICATION AND DELETE DATA
cur.execute('SELECT id FROM myClass WHERE nazwa = ?', ('1B', ))
klasa_id = cur.fetchone()[0]
cur.execute('UPDATE uczen SET myClass_id=? WHERE id=?', (klasa_id, 2))


cur.execute('DELETE FROM uczen WHERE id=?', (3,))

readData()
