name = "Senanur"
surname ="KORKMAZ"
age = 21
print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {n} {s}".format(n=name,s=surname))
print("My name is {} {} and I'am {} years old.".format(name, surname, age))
print("My name is {} {} and I'am {} years old.".format(name,name,name))
result = 200/700
print('the result is {r}'.format(r=result))
print('the result is {r:1.4}'.format(r=result))
print('the result is {r:10.4}'.format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old. ")