# install postgres and pgadmin gui to machine from postegres website
import psycopg2


def create_table():
    # 1.connect to a database
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"
    )

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
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    insert_query = """ INSERT INTO store VALUES (%s,%s,%s) """
    record_to_insert = (item, quantity, price)
    cur.execute(
        insert_query, record_to_insert
    )
    conn.commit()
    conn.close()


# view data from db
def view():
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # fetch data from db
    rows = cur.fetchall()  # will return a python list
    conn.close()
    return rows


# delete data from db
def delete(item):
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


# update data
def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# insert('apple', 1, 1)
# delete("apple")
# update(20, 100, "orange")
print(view())
