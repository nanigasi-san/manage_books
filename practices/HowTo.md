## データベースのおさらい

### 表の作成：CREATE文
```sql
CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT)
```

### 行データの挿入
```sql
INSERT INTO books (title, author)
VALUES ('プリンキピア','ニュートン')
```

### 表データの検索
```sql
SELECT * FROM books
```
---