def usalma(number):
    def inner(power):
        return number**power
    return inner

#two usalma fonksiyonunun 2 almis hali oluyor 
# inner fonksiyonu gibi kullaniliyor
print(usalma)
two = usalma(2)
three = usalma(3)
print('two:',two)
print('three:',three)
print(two(3))
print(three(3))
print('---------------------------------')

def yetki_sorgula(page):
    def inner(role):
        if role.lower() == 'admin':
            return '{0} rolu {1} sayfasina ulasabilir.'.format(role,page)
        else:
            return '{0} rolu {1} sayfasina ulasamaz.'.format(role,page)
    return inner

user1 = yetki_sorgula('Product Edit')
print(user1('Admin'))
print(user1('User'))
print('---------------------------------')

def islem(islem_adi):
    def toplama(*args):
        toplam = 0 
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    if islem_adi.lower() == 'carpma':
        return carpma
    elif islem_adi.lower() == 'toplama':
        return toplama

islem1 = islem('Toplama')
print(islem1(4,3,5,6))
islem2 = islem('Carpma')
print(islem2(4,5,0))
