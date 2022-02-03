#class
class Person:
    #class attributes
    address = 'no information'

    #constructor
    def __init__(self,name,year):

        #object attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('Hello There. I am '+self.name)
    def calculateAge(self):
        return 2019 - self.year

#object (instance)
p1 = Person(name='ali',year=1990)
p2 = Person(name='yagmur',year = 1995)
p1.intro()
print(f'Yasim: {p1.calculateAge()}')
p2.intro()
print(f'Yasim: {p2.calculateAge()}')
#accessing object attributes
print(f'p1 name:{p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 name:{p2.name} year: {p2.name} address: {p2.address}')