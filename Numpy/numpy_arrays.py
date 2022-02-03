import numpy as np

result = np.array([1,3,5,7,9])
print(result)

result = np.arange(1,10)
print(result)

result = np.arange(10,100,3)
print(result)

#verilen sayida 0 iceren dizi dondurur
result = np.zeros(10)
print(result)

#verilen sayida 1 iceren dizi dondurur
result = np.ones(20)
print(result)

#linespace verilen araligi 5(parametre degistirilebilir) esit parcaya boler
result = np.linspace(0,100,5)
print(result)
result = np.linspace(0,5,5)
print(result)

# 0 dan 10 a kadar (10 dahil degil) random bir sayi turetir
result = np.random.randint(0,10)
print(result)
result = np.random.randint(20)
print(result)

#1 den 10 a kadar olan sayilardan random 3 tane sayiyi alir ve bir array olusturur
result = np.random.randint(1,10,3)
print(result)

#0 ile 1 arasinda 10 adet random sayi olusturur randn ise negatifi dahil eder 
result = np.random.rand(10)
print(result)
result = np.random.randn(10)
print(result)

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi)

#satirlarin toplami
print(np_multi.sum(axis=1))

#sutunlarin toplami
print(np_multi.sum(axis=0))

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
rnd_max = rnd_numbers.max()
print(rnd_max)
rnd_min = rnd_numbers.min()
print(rnd_min)
rnd_avarage = rnd_numbers.mean()
print(rnd_avarage)

#indexini ogrenmek icin
rnd_min_index = rnd_numbers.argmin()
print(rnd_min_index)


