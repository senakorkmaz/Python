import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()

sql = 'SELECT * FROM albums'
cursor.execute(sql)
liste = cursor.fetchall()

for item in liste:
    print(item[0],item[1],item[2])
connection.close()