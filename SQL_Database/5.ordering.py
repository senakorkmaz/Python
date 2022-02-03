from cv2 import error
import mysql.connector

def order():
    connection = mysql.connector.connect(host='localhost',user='root',password='sena1234',database='node-app')
    cursor = connection.cursor()

    #istedigimiz kolona gore siralama yapar
    #Sonuna DESC eklersek tersten siralar 
    cursor.execute('select * from products Order By price DESC')
    
    try:
        result = cursor.fetchall()

        for product in result:
            print(product)

    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print('\nDatabase baglantisi kapandi')

order()