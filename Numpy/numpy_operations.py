import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

#ayni indexteki elemanlari birbiriyle toplar
sumNumpyArray = numbers1 + numbers2
print(sumNumpyArray)

#butun elemanlara 10 ekler
sum = numbers1 + 10
print(sum)

#ayni indexteki elemanlari birbirinden cikarir
subNumpyArray = numbers1 - numbers2
print(subNumpyArray)

divNumpyArray = numbers1 / numbers2
print(divNumpyArray)

multiNumpyArray = numbers2*numbers1
print(multiNumpyArray)

sinNp = np.sin(numbers1)
print(sinNp)
cosNp = np.cos(numbers1)
print(cosNp)
sqrtNp = np.sqrt(numbers1)
print(sqrtNp)
logNp = np.log(numbers1)
print(logNp)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

#dikey olarak birlestirme
result = np.vstack((mnumbers1,mnumbers2))
print(result)
#yatay olarak birlestirme
result = np.hstack((mnumbers1,mnumbers2))
print(result)

#20 ye esit veya buyuk degerler icin true degerini sakalyan dizi dondurur
result = (numbers1 % 2) == 0
print(result)

print(numbers1[result])

