import sqlite3

dbpath = 'E:/Donnees/Programmation/dofus-trading-database/dofus-trading.db'
conn = sqlite3.connect(dbpath)
truc = 'chapeau'
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS """+truc+"""(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO chapeau(name, age) VALUES(?, ?)""", ("machin", 30))

users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO chapeau(name, age) VALUES(?, ?)""", users)

id = cursor.lastrowid
print('dernier id: %d' % id)

cursor.execute("""SELECT id, name, age FROM chapeau""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

cursor.execute("""SELECT id, name, age FROM chapeau""")
for row in cursor:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

conn.commit()
conn.close()
