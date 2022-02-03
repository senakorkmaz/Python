import mysql.connector

def deleteProduct(id):
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    sql='DELETE from products where id=%s'
    params = (id,)
    cursor.execute(sql,params)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit silindi.')
    except mysql.connector.Error as err:
        print('Bir hata olustu',err)
    finally:
        connection.close()
        print('Database baglantisi kapandi')
    pass

id = input('Silmek istediginiz urunun idsi :')
deleteProduct(id)