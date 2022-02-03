import numpy as np

numberss = np.array([0,5,10,15,20,25,50,75])

result = numberss[5]
print(result)

result = numberss[-5]
print(result)

result = numberss[:3]
print(result)

result = numberss[3:]
print(result)

result = numberss[::]
print(result)

result = numberss[::-1]
print(result)

numberss2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numberss2)

#satira ulasmak icin
result = numberss2[0]
print(result)

#sutuna ulasmak icin
result = numberss2[:,0]
print(result)

#belirli elemana ulasmak icin
result = numberss2[0,2]
print(result)

#0. sutundan baslayip 1. stuna kadar toplam 2 sutunu yazdirdi
result = numberss2[:,0:2]
print(result)

#son satirdaki tum sutunlar
result = numberss2[-1,:]
print(result)

#2 ye 2 ilk satir ve stunlardan bir matrix olusturdu
result = numberss2[:2,:2]
print(result)



arr1 = np.arange(0,10)
#pointer mantigi var
#arr2 = arr1

#burada pointer yok sadece degerleri kopylar
arr2 = arr1.copy()
print(arr1)
print(arr2)
arr1[0]=10
arr2[1]=20
print(arr1)
print(arr2)