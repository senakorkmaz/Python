def SayHello(name = 'name'):
    print('Hello',name)

SayHello()
SayHello('Sena')

def change(n):
    n[0]='istanbul'

sehirler = ['ankara','mardin']
change(sehirler[:])
print(sehirler)
change(sehirler)
print(sehirler)

#istenilen miktarda parametre gonderilebilir
def add(*params):
    print(params)
    sum = 0
    for n in params:
        sum += n
    return sum

print(add(1,2))
print(add(1,3,6,9))

def allValue(a,b,*list,**dictionaries):
    print(a)
    print(b)
    print(list)
    print(dictionaries)

allValue(10,20,30,40,50,key1 = 'value1',key2= 'value2')