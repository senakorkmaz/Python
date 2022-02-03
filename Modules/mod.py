def FirstFactorial(num):
  # code goes here
  number = num
  for a in range(1,number):
        num = num*(number - a)
  
  return num

# keep this function call here 
print(FirstFactorial(int(input())))