myList = ["1","2","5a","10b","abc","10","50"]
#1: myList elemanlari icindeki sayisal degerleri bulunuz.
def findNumeric(list):
    for i in range(0,len(list)):
        try:
            a = int(list[i])
        except ValueError:
            pass
        else:
            print(a)
#findNumeric(myList)

#2: Kullanici 'q' degerini girmedikce aldiginiz her inputun 
#sayi olduguna emin olun aksi halde hata mesaji verin
def findNumber():
    while True: 
        try:
            a = input('Bitirmek icin "q" ya basiniz:')
            if(a == 'q'):
                break
            a = int(a)

        except ValueError:
            print('Sadece sayi giriniz')
#findNumber()

#3: Girilen parola icinde Turkce karakter hatasi veriniz
def findChar(psw):
    import re
    if re.search('[ĞÜİÖÇŞğüşıöç]',psw):
        raise Exception('Sifreniz Turkce karakter icermekte!!')
try:
    findChar('ergfeenge')
except Exception as ex:
    print(ex)
else:
    print('Parola islemi basarili')

#4: Faktoriyel fonksiyonu olusturup fonksyona gelen deger icin 
#hata mesaji olusturun
def findFactorial(num):
    number = int(num)
    if num < 0 :
        raise Exception('Negatif deger.')
    for i in range(1,int(num)):
        number = number*(num - i)
    return number
try:
    print(findFactorial(-2))
except ValueError :
    print('Lutfen sadece sayi girisi yapiniz.')
except Exception as ex:
    print(ex)


