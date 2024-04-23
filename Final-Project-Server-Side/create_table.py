# Open a python terminal and execute this script:
# python create_table.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE receipts (name TEXT, addr TEXT, city TEXT, zip TEXT, quantity TEXT, price TEXT, date TEXT)')
print("Created table successfully!")

conn.close()

