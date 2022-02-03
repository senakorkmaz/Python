def toplama(a,b):
    return (a+b)
def cikarma(a,b):
    return (a-b)
def carpma(a,b):
    return (a*b) 
def bolme(a,b):
    return (a/b)

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi.lower() == 'toplama':
        print(f1(1,2))
    elif islem_adi.lower() == 'cikarma':
        print(f2(3,1))
    elif islem_adi.lower() == 'carpma':
        print(f3(3,1))
    elif islem_adi.lower() == 'bolme':
        print(f4(5,2))
    else:
        print('Hatali islem adi')

islem(toplama,cikarma,carpma,bolme,'Toplama')
islem(toplama,cikarma,carpma,bolme,'cikarma')
islem(toplama,cikarma,carpma,bolme,'carpma')
islem(toplama,cikarma,carpma,bolme,'bolme')
islem(toplama,cikarma,carpma,bolme,'islem')
