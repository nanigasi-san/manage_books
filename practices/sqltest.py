import sqlite3

CREATE_TABLE = '''CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT)
'''

TEST_INSERT = '''INSERT INTO books (title, author)
VALUES ('プリンキピア','ニュートン')
'''

TEST_SELECT = "SELECT * FROM books"

conn = sqlite3.connect("testdb.sqlite3")
c = conn.cursor()
c.execute(CREATE_TABLE)
c.execute(TEST_INSERT)
conn.commit() # 書き込みの確定
c.execute(TEST_SELECT,)
result = c.fetchone()
print(result)
conn.close()