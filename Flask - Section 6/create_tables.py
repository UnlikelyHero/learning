import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# creating users table using the id as a primary key
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,    username text, password text)"
cursor.execute(create_table)

# creating items table using item_id as the primary key
create_table = "CREATE TABLE IF NOT EXISTS items (item_id text PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
