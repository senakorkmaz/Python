sayilar = [1,3,5,7,9,12,19,21]
#Sayilar listesini whlie ile ekrana yazdirin
i = 0
while i<len(sayilar):
    print(sayilar[i])
    i +=1
print('--------------------------------------')
#Baslangic ve bitis degerini kullanicdan alip aradaki tum
# tek sayilari ekrana yazdirin.
baslangic = int(input('Baslangic degeri:'))
bitis = int(input('Bitis degeri: '))
sayi = baslangic+1
print('Tek Sayilar;')
while sayi < bitis:
    if sayi%2 != 0:
        print(sayi)
    sayi +=1

print('---------------------------------------')
#1-100 arasindaki sayilari azalan sekilde yazdir

sayi = 100
while sayi>=0:
    #print(sayi)
    sayi -=1

#Kullanicidan alacaginiz 5 sayiyi ekrana sirali bir sekilde yazdirin
i = 0
gelen = []
while i<5:
    sayi = int(input(f'{i}. sayiyi giriniz:'))
    gelen.append(sayi)
    i +=1

gelen.sort()
print(gelen)


print('-----------------------------------------------')
urunler = []
adet = int(input('Girilecek urun sayisi: '))
i = 0

while i<adet:
    name = input('Urunun adini giriniz:')
    price = input('urunun fiyatini giriniz:')
    urunler.append({
        'name': name,
        'price':price
    })
    i +=1

for urun in urunler:
    print(f'Urunun adi: {urun["name"]} Urunun fiyati: {urun["price"]}')