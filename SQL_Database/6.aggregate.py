import mysql.connector

def aggregate():
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()
   
    sql='select COUNT(*) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('result:',result[0])

    sql='select COUNT(name) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('result:',result[0])  

    sql='select COUNT(*) from products where price>1000 '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('where price>1000:',result[0])
    
    sql='select AVG(price) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('AVG(price):',result[0])

    sql='select sum(price) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('sum(price):',result[0])

    sql='select max(price) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('max(price):',result[0])

    sql='select min(price) from products '
    cursor.execute(sql)
    result = cursor.fetchone()
    print('min(price):',result[0])

    sql='SELECT name FROM products WHERE price = (SELECT max(price) FROM products)'
    cursor.execute(sql)
    result = cursor.fetchone()
    print('Max price name:',result[0])

aggregate()