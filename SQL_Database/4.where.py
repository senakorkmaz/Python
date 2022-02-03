import mysql.connector

def filterProducts():
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    cursor.execute('select * from products where name LIKE "%Samsung%" and price=2000')
    #basinda % olmazsa sadece samsung ile baslayanlari
    #sonunda % olmazsa sadece samsung ile bitenleri
    product = cursor.fetchall()
    if len(product) == 1:
        print(product[0])
    else:
        for pro in product:
            print(pro)
def filterProductsById(id):
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()
    sql='select * from products where id = %s'
    params =(id,)
    cursor.execute(sql,params)
    product = cursor.fetchone()
    print(product)

filterProductsById(4)