for i in range(5,50,10):
    print(i)

#enumerate
greeting = 'Hello There'

for index,letter in enumerate(greeting):
    print(f'Index : {index} Letter: {letter}')

#zip
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

list3 = list(zip(list1,list2))
print(list3)

for item1, item2 in list(zip(list1,list2)):
    print(item1,item2)