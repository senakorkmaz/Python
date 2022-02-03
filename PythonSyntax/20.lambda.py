def square(num): return num**2

numbers = [1,3,5,7,6,8]

#map
result = list(map(square,numbers))
print('square:',result)

#lambda
result = list(map(lambda num: num**3,numbers))
print('lambda:',result)

lambdaSquare = lambda num : num**2
result = list(map(lambdaSquare,numbers))
print('lambdaSquare:',result)

#filter
def check_even(num): return num%2==0

result=list(filter(check_even,numbers))
print(result)