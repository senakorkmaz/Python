from datetime import datetime

name = 'sena'
print('benim adim %s',name)

list = [
    ('301','Ahmet','Yilmaz',datetime(2005,5,17),'E'),
    ('302','Ali','Can',datetime(2005,6,17),'E'),
    ('304','Canan','Tan',datetime(2005,7,17),'K'),
    ('305','Ayse','Taner',datetime(2005,9,17),'K'),
    ('306','Bahadir','Toksoz',datetime(2004,7,27),'E'),
    ('307','Ali','Cenk',datetime(2003,8,25),'E')
      ]
values =[]
order = [1,2,3,4,0]

for item in list:
    print(item)
    item = [item[i] for i in order]
    print(item)
    values.append(item)