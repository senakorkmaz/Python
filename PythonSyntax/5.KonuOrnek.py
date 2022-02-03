website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
name, surname, age, job = 'Bora','Yilmaz',32,'muhendis'
#1-Course karakter dizisinde kac karakter bulunmaktadir ?
print(len(course))

#2- website icinden www karakterlerini alin.
print(website[7:10])

#3- website icinden com karakterini alin.
print(website[22:25])
print(website[len(website)-3:len(website)])

#4- course icinden  ilk 15 ve son 15 karakterlerini alin.
ilk15 = course[0:15]
son15 = course[len(course)-15:]
print(f"Ilk 15 :{ilk15} \nSon 15:{son15}")

#5- course ifadesindeki karakterleri terseten yazdirin.
print(course[::-1])
s = '12345'*5
print(s)
print(s[::5])

#6- Benim adim Bora Yilmaz, Yasim 32 vee meslegim muhendis yazdir
print(f"Benim adim {name} {surname}, Yasim {age} ve meslegim {job}")

#7- 'Hello world' ifadesindeki w harfini W ile degistirin.
s = 'Hello world'
s = s[:6] + 'W' + s[-4:]
print(s)
s.replace('w','W')

#8- 'abc' ifadesini yan yana 3 defa yazdir.
abc = 'abc'
print(f"{abc} {abc} {abc}")
print(abc*3)
