#1- "Bmw, Mercedes, Opel, Mazda" elemanlarina sakip bir liste olusturunuz
my_list = ['Bmw','Mercedes','Opel','Mazda']

#2- Liste kac elemanlidir 
print(len(my_list))

#3- Listenin ilk ve son elemani nedir
print("Ilk elemani: ",my_list[0])
print("Son elemani: ",my_list[len(my_list)-1])
print("Son elemani: ",my_list[-1])

#4- Mazda dergerini Toyota ile degsistirin
print(my_list)
my_list[3] = 'Toyata'
print(my_list[3])
print(my_list)

#5- Mercedes listenin bir elemani midir 
print(my_list.index('Mercedes'))
print('Mercedes' in my_list)

#6- Listenin -2 indexli degeri nedir
print(my_list[-2])
#7- Listenin ilk 3 elemanini alin 
print("Listenin ilk 3 elemani: ", my_list[0:3])

#8- Listenin son iki elamninin yerine Toyota ve Renault degerlerini ekleyin
my_list[-2:] = ['Toyota','Renault']
print(my_list)

#9- Listenin uzerine Audi ve Nissan degerini ekleyin
my_list.append("Audi")
my_list.append("Nissan")
print(my_list)

#10- Listenin son elemanini silin
my_list.remove(my_list[-1])
print(my_list)

#11- Listenin elemenlarini tersten yazdirin
print(my_list[::-1])

