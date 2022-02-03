list = [1,2,3,4,5,6]
iterator = iter(list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
print("-----------------------")
iterator = iter(list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start +=1
            return x
        else:
            raise StopIteration

number = MyNumbers(20,30)

for i in number :
    print(i)

myiter = iter(number)
while True:
    try:
        print(next(myiter))
    except StopIteration:
        break