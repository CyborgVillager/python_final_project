import sqlite3


# connection tot he database/creating if not exist
def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, '
                'author text, year integer , isbn integer, price float, quantity integer)')
    conn.commit()
    conn.close()


# deleting information on user request
# id=? -> colum name   (id,) -> function parameter
# its the arg valu delete(id)
def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()


# inserting information & connecting to db
# get the tuple
def insert(title, author, year, isbn, price, quantity):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?,?,?)', (title, author, year, isbn, price, quantity))
    conn.commit()
    conn.close()


# updating records
# by the row from the display box
def update(id, title, author, year, isbn, price, quantity):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=?,price=?, quantity=? WHERE id=?',
                (title, author, year, isbn, price, quantity, id))
    conn.commit()
    conn.close()

def addto_cart(id, title, author, year, isbn, price, quantity):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=?,price=?, quantity=? WHERE id=?',
                (title, author, year, isbn, price, quantity, id))
    conn.commit()
    conn.close()

# viewing information fetch all rows from the able
def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows


connect()
# printing the statement
# insert('Choco','Eth Henr', 13212, 44131)
# delete by the id
# delete(1)
# update information
# update(2,'The moon','Jake Kent', 2019 , 14414)
print(view())
# searching for an arg
# print(search(author='Eth Henr'))
