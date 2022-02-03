#Identity Operator : is
print('k = l =[1,2,3]')
print('m =[1,2,3]')
k = l =[1,2,3]
m = [1,2,3]

print('k is l :',k is l)
print('k == l :', k == l)

print('k is m :', k is m)
print('k == m :', k == m)
print('k is not m :', k is not m)
print('-------------------------------')

#Membership Operator : in
q = ['apple', 'banana']
print('q:',q)
print('banana in q:','banana' in q)
print('Strawberry in q:','Strawberry' in q)

print('-------------------------------')
x = 4

print('x is greater than 3 and less than 6:',3<x<6)

#and
print('x is greater than 2 and less than 7:',(2<x) and (x<7))

#or
print('x is greater than 4 or greater than 1:',(x>4) or (1<x))

#not
print('x is less than 7:',not(x>7))


