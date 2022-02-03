numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

names = ['cinar','sadik','sena']

for name in names:
    print(f'My name is {name}.')

tuple = [(1,2),(3,4),(5,7)]

for a,b in tuple:
    print(a,b)

d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(f'Key: {key} Value: {value}')

#loops examples
print('-------------EXAMPLES--------------')
#3 un kati olan sayilari toplamini ve tek sayilarin karesini al
Sayilar = [1,3,5,6,9,12,19,21]
toplam = 0

for sayi in Sayilar:
    toplam +=sayi
    if ((sayi%3) == 0) and ((sayi%2) != 0):
        print(f'{sayi} ucun kati ve tektir. Karesi: {sayi*sayi}')
    elif (sayi%3) == 0:
        print(f'{sayi} ucun katidir.')
    elif (sayi%2) != 0:
        print(f'{sayi} tektir. Karesi: {sayi*sayi}')
    
print(f'Sayilar dizisinin toplami: {toplam}')
print('----------------------------------------------------')
#Sehirlerden hangileri en fazla 5 karakterlidir
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
for sehir in sehirler:
    if len(sehir) <= 5:
        print(f'{sehir} en fazla 5 karakterlidir.')
print('-----------------------------------')
urunler = [
    {'name':'samsung S6','price':3000},
    {'name':'samsung S7','price':4000},
    {'name':'samsung S8','price':5000},
    {'name':'samsung S9','price':6000},
    {'name':'samsung S10','price':7000}
]
toplamFiyat = 0
#urunlerin fiyatlari toplamini yazdir 
#fiyatlari en fazla 5000 olan urunleri goster 
for urun in urunler:
    toplamFiyat += urun['price']
    if urun['price'] <= 5000:
        print(urun)

print(f'Urunlerin fiyat toplami: {toplamFiyat}')

for i in range(10):
    print(i)