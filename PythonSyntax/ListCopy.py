
li1 = [1,2,3,4,5,6]
li2 = li1
li3 = li1.copy()
print("------Değişiklik Yapmadan Önce------")
print("li1:",li1)
print("li2:",li2)
print("li3:",li3)
print("------Değişiklik Yaptıktan Sonra------")
li1[2]=90
print("li1:",li1)
print("li2:",li2)
print("li3:",li3)