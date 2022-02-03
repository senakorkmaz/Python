import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', # 192.23.45.56
    user = 'root',
    password = 'sena1234',
    database ='node-app'
)

mycursor = mydb.cursor()
#Database olusturma 
#mycursor.execute('CREATE DATABASE mydatabase')

# mycursor.execute('SHOW DATABASES')

# for x in mycursor:
#     print(x)

#mycursor.execute('CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))')