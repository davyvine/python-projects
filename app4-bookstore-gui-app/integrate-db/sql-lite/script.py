# sql lite is python built in lib
import sqlite3


def create_table():
    # 1.connect to a database
    conn = sqlite3.connect("lite.db")

    # 2.create cusrsor object
    cur = conn.cursor()

    # 3. write an sql query
    # create table - store is the name of table,
    cur.execute(
        # pass query in a ""
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
    )

    # 4. commit changes to db
    conn.commit()

    # 5. close connection
    conn.close()

# insert values in table columns


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    conn.execute(
        "INSERT INTO store VALUES (?,?,?)", (item, quantity, price)
    )
    conn.commit()
    conn.close()


# view data from db
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # fetch data from db
    rows = cur.fetchall()  # will return a python list
    conn.close()
    return rows


# delete data from db
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


# update data
def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()


update(20, 100, "water glass")
print(view())
