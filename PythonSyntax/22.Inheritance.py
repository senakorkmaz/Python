class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print('Student Created')
    #override
    def who_am_i(self):
        print('I am a student')
    
p1 = Person('Ali','Yilmaz')
s1 = Student('Cinar','Turan',1256)

print(f'{p1.firstName} {p1.lastName} ')
print(f'{s1.firstName} {s1.lastName} {s1.studentNumber}')

p1.who_am_i()
p1.eat()
s1.who_am_i()
s1.eat()        

        