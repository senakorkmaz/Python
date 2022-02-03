def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan onceki islemler")
        func(name)
        print("Fonksiyondan sonraki islemler")
    return wrapper

@my_decorator
def sayHello(name):
    print("Hello",name)


def sayGreeting():
    print("Greeting")

sayHello("senanur")

# sayHello = my_decorator(sayHello)
# sayHello()

# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()

import math
import time
def new_decorator(func):
    def wrapper(*arg):
        start = time.time()
        time.sleep(1)
        func(*arg)
        finish = time.time()
        print('Fonksiyon '+str(finish-start)+' saniye surdu')
    return wrapper
@new_decorator
def usalma(a,b):
    print(math.pow(a,b))

@new_decorator
def faktoriyel(num):
    print(math.factorial(num))
@new_decorator
def sum(a,b):
    print(a+b)
usalma(2,3)
faktoriyel(3)
sum(2,4)