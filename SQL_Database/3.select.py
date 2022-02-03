from matplotlib.pyplot import connect
import mysql.connector

def insertProduct(name, price,imageUrl,description):
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name,price,imageUrl,description) VALUE (%s,%s,%s,%s)'
    values = (name,price,imageUrl,description)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit eklendi.')
        print(f'Son eklenen kaydin id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Bir hata olustu',err)
    finally:
        connection.close()
        print('Database baglantisi kapandi')
    pass

def insertProducts(pList):
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name,price,imageUrl,description) VALUE (%s,%s,%s,%s)'
    values = pList
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit eklendi.')
        print(f'Son eklenen kaydin id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Bir hata olustu',err)
    finally:
        connection.close()
        print('Database baglantisi kapandi')
    pass

def getProducts():
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    cursor.execute('select name,price from products')

    #products = cursor.fetchall()
    products = cursor.fetchone()
    # for product in products:
    #     print(product)
    print(products)

getProducts()