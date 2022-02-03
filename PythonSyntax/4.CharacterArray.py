name = 'Senanur'
surname = 'Korkmaz'
age = 21

greeting = 'My name is '+ name + ' ' + surname + ' and \nI am ' + str(age)+ ' years old.'
lenght = len(greeting)

print(greeting)
print(greeting[1])
print(len(greeting))
print(greeting[lenght-1])
print(greeting[-1])
#3, index dahil fakat 6. index dahil degil
print(greeting[3:6])
print(greeting[3:])
print(greeting[2:40:3])