'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyadi': 'Yilmaz',
            'telefon': '532 000 00 01'
        },
    }
    1- Kullanicidan alinan bilgilerle yukardaki gibi bir dictionary olusturunuz
    2- Ogrenci numarasini kullanicidan alip ilgili ogrenci bilgisini gosterin
'''
ogrenciler =  {} 

number = input('Ogrenci no: ')
name = input('Ogrenci adi: ')
surname = input('Ogrenci soyadi:')
phone = input('Orenci telefon: ')

'''
ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone,
}
'''

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone,
    }
})

print(ogrenciler)