website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello Workd ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin
print(' Hello World '.strip())
print(' Hello World '.lstrip())
print(' Hello World '.rstrip())

#2- 'www.sadikturan.com' icindeki sadikturan bilgisi haricindeki her karakteri silin
print('www.sadikturan.com'.lstrip('www.').rstrip('.com'))
print('www.sadikturan.com'.strip('w.moc'))

#3- 'course' karakter dizisinin tum karakterlerini kucuk yap
print(course.lower())

#4- website icinde kac tane a karakteri vardir 
print(website.count('a'))

#5- website www ile baslayip com ile bitiyor mu ?
print(website.startswith('www'),course.endswith('.com'))


#6- website icerisinde .com ifadesi var mi ?
print(website.find('.com'))
print(website.index('.com'))

#7- course icindeki karakterlerin hepsi alfabetik mi ?
print("Course is alpha ? ",course.isalpha())
print("Course is digit ? ",course.isdigit())

#8- 'Contents' ifadesinin satirda 50 karakter icine yerlestirip sag ve soluna * ekleyiniz
print("Contents".center(50,'*'))
print("Contents".ljust(50,'*'))
print("Contents".rjust(50,'*'))
#9- course karakter dizisindeki tum bosluk karakterlerini '-' ile degistiriniz
print(course.replace(' ','-'))
print(course.replace(' ','-',3))

#10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak  degistirin 
print('Hello World'.replace('World','There'))

#11- course karakter dizisini bosluk karakterlerinden ayiriniz
print(course.split(' '))

