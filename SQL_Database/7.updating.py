import mysql.connector

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    sql='UPDATE products SET name = %s ,price=%s where id=%s'
    params = (name,price,id)
    cursor.execute(sql,params)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit guncellendi.')
    except mysql.connector.Error as err:
        print('Bir hata olustu',err)
    finally:
        connection.close()
        print('Database baglantisi kapandi')
    pass

id = input('Degisim yapmak istediginiz urunun idsi :')
name = input('Yeni adi:')
price = input('Yeni fiyati:')
updateProduct(id,name,price)