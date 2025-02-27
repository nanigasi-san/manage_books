import sqlite3
DROP_TABLE="DROP TABLE IF EXISTS books"

CREATE_TABLE="""CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT,
genre TEXT,
lending BOOLEAN,
username TEXT,
timestamp TEXT)"""

TEST_INSERT="""INSERT INTO books (title, author, genre, lending, username, timestamp)
VALUES ('プリンキピア','ニュートン','物理',FALSE,'','')"""

TEST_SELECT="SELECT * FROM books"

conn = sqlite3.connect("bookdb.sqlite3")
c = conn.cursor()

c.execute(DROP_TABLE)
c.execute(CREATE_TABLE)
c.execute(TEST_INSERT)

conn.commit()

c.execute(TEST_SELECT)
result = c.fetchone()
print(result)
conn.close()