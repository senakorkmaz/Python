numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))


print(numbers[3:6])
print(numbers[:3])
print(numbers[4:])

#Adds an element at the end of the list
numbers.append(34)
print(numbers)
numbers.insert(3,78)
print(numbers)
numbers.insert(-1,44)
print(numbers)

#Removes the element at the specified position
numbers.pop()
print(numbers)

numbers.pop(5)
print(numbers)

#Removes the first item with the specified value
numbers.remove(10)
print(numbers)

#Sorts the list
numbers.sort()
letters.sort()
print(numbers)
print(letters)

#Reverses the order of the list
numbers.reverse()
print(numbers)