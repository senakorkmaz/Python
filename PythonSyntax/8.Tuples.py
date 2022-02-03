myTuple = ('1',2,'3')
print(myTuple)

#Tuples are unchangeable but you can convert the tuple into a list
myList = list(myTuple)
myList[0] = 0
myTuple = tuple(myList)
print(myTuple)

#Tuples are immutable, they do not have a build-in append() method 
# you can convert the tuple into a list, add your item
myList = list(myTuple)
myList.append(3)
myTuple = tuple(myList)
print(myTuple)

#Add tuple to a tuple. You are allowed to add tuples to tuples
#so if you want to add one item, (or many), create a new tuple with the item(s), 
# and add it to the existing tuple
myNewTuple = (4,5,6)
myTuple += myNewTuple
print(myTuple)

#Multiply Tuples
myMultiTuple = myTuple*2
print(myMultiTuple)

#Tuples are unchangeable, so you cannot remove items from it, 
# but you can use the same workaround as we used for changing and adding tuple items
#Or you can delete the tuple completely
del myNewTuple
print(myNewTuple) #this will raise an error