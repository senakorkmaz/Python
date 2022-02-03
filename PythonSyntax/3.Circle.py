'''
 Circle area = pi*r*r
 Circle  Perimeter = 2*pi*r
 pi=3.14
'''
r = input('Radius: ')
pi = 3.14

areaOfCircle = pi*(float(r)**2)
perimeterOfCircle = 2*pi*float(r)

print("Area Of Circle: " + str(areaOfCircle))
print("Perimeter Of Circle: ", str(perimeterOfCircle))

