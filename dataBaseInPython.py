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
cur.execute('SELECT id FROM myClass WHERE nazwa = ?', ('1A',))
klasa_id = cur.fetchone()[0]

# "uczniowie" tuple include tuple with students data
uczniowie = (
        (None, 'Tomasz', 'Nowak', myClass_id),
        (None, 'Jan', 'Kos', myClass_id),
        (None, 'Piotr', 'Kowalski', myClass_id)
        )

# adding multiple records
cur.executemany('INSERT INTO uczen VALUES(?,?,?,?)', uczniowie)

# commit in DB
con.commit()


