import sqlite3

conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("machin", 30))

users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)

id = cursor.lastrowid
print('dernier id: %d' % id)

cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

cursor.execute("""SELECT id, name, age FROM users""")
for row in cursor:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

conn.close()
