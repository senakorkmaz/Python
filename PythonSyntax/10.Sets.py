#Set is a collection which is both unordered and unindexed
#Dublicates not allowed
mySet = {'Banana', 1,'Apple',False}
print(mySet)
print(len(mySet))
print(type(mySet))

#We can use to set() constructor to make a set
thisSet = set(('banana', True,False))
print(thisSet)
print(type(thisSet))

#Add items
mySet.add('Orange')
print(mySet)

#Add Sets
mySet.update(thisSet)
print(mySet)

#Add Any Iterable
myList = ['1',2]
mySet.update(myList)
print(mySet)

for x in mySet:
    print(x)

#Remove Items
mySet.remove('Banana')
mySet.discard('banana')
print(mySet)
mySet.pop()
print(mySet)
mySet.clear()
print(mySet)