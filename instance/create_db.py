import sqlite3
DROP_TABLE="DROP TABLE IF EXISTS books"

CREATE_TABLE="""CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT,
genre TEXT)"""

TEST_INSERT="""INSERT INTO books (title, author, genre)
VALUES ('プリンキピア','ニュートン','物理')"""

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