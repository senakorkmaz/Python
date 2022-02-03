import mysql.connector

def join():
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    sql = 'SELECT * FROM products'
    sql = 'SELECT * FROM categories'
    sql = 'SELECT * FROM products inner join categories on categories.id = products.categoryid '
    sql = 'SELECT products.name, products.price, categories.name FROM products inner join categories on categories.id = products.categoryid '
    sql = 'SELECT products.name, products.price, categories.name FROM products inner join categories on categories.id = products.categoryid where categories.name="Telefon"'
    sql = 'SELECT p.name, p.price, c.name FROM products as p inner join categories as c on c.id = p.categoryid where p.price>2000'
    cursor.execute(sql)
    
    try:
        result = cursor.fetchall()

        for product in result:
            print(product)

    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print('\nDatabase baglantisi kapandi')

join()