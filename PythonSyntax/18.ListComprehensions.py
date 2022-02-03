numbers = []
for x in range(10):
    numbers.append(x)
print('Numbers:',numbers)

#---------------------------------
numbers1 = [x for x in range(10)]
print('Numbers1:',numbers1)

#---------------------------------
numbers2 = [x**2 for x in range(10)]
print('Numbers2:',numbers2)

#---------------------------------
numbers3 = [x*x for x in range(10) if x%3 == 0]
print('Numbers3:',numbers3)

#---------------------------------
myString = 'Hello'
myList = [letter for letter in myString]
print('MyList: ',myList)

#---------------------------------
years = [1983, 1999,2008, 1956, 1986]
age =[2021-x for x in years]
print('Age:',age)
#---------------------------------
result = [x if x%2 == 0 else 'Tek' for x in range(10)]
print('Result: ',result)
#-----------Demo------------------
import random
randomNumber = random.randrange(1,100)
i = 0
puan = 100
gelen = int(input('Kac tahmin yapacaksiniz :'))
print(randomNumber)
while i<gelen:
    tahmin = int(input('Sayi tahmininizi giriniz:'))
    if randomNumber == tahmin:
        puan = puan - (puan/gelen)*i
        print(f'Dogru bildiniz puaniniz:{int(puan)}')
        break
    i+=1
    if (randomNumber != tahmin) and (i == gelen):
         print('Bilemediniz Puaniniz: 0')

