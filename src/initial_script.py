import sqlite3
conn = sqlite3.connect('data_store.db')

conn.execute("CREATE TABLE STORE (ID INTEGER PRIMARY KEY AUTOINCREMENT, KEY TEXT NOT NULL, DOCUMENT TEXT NOT NULL)")

print ("Table created successfully")

conn.close()