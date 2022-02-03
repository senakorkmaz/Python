import turtle
import time

def circle (turtlee,size):
  turtlee.forward(30)
  turtlee.left(90)
  for i in range(90):
    turtlee.forward(size)
    turtlee.right(6)
  turtlee.left(90)

def box(turtlee,zero,text):
  turtlee.forward(30)
  turtlee.left(90)
  turtlee.forward(15)
  for i in range(3):
    turtlee.right(90)
    turtlee.forward(30)
  turtlee.right(90)
  turtlee.forward(15)
  turtlee.right(90)
  turtlee.penup()
  turtlee.forward(15/2)
  turtlee.pendown()
  if zero == False:
    turtlee.write(text)
  turtlee.penup()
  turtlee.forward((15/2)*3)
  turtlee.pendown()
  

def geriDon1(turtlee,box):
    turtlee.penup()
    turtlee.forward((box*60))
    turtlee.pendown()
    
def geriDon2(turtlee,box):
    turtlee.penup()
    turtlee.backward((box*60))
    turtlee.pendown()

def ustCiz(turtlee,size,ustzsize,zero,deger):
    turtlee.left(90)
    turtlee.forward(size)
    turtlee.right(90)
    box(turtlee,zero,deger)
    if zero:
        turtlee.penup()
    turtlee.forward((ustzsize)*60)
    turtlee.right(90)
    turtlee.forward(size)
    turtlee.left(90)
    geriDon2(turtlee,ustzsize)

def altCiz(turtlee,size,altzsize,zero,deger):
    turtlee.right(90)
    turtlee.forward(size)
    turtlee.right(90)
    box(turtlee,zero,deger)
    if zero:
        turtlee.penup()
    turtlee.forward((altzsize)*60)
    turtlee.right(90)
    turtlee.forward(size)
    turtlee.right(90)
    geriDon1(turtlee,altzsize)



print('******************************************************************************************')
print("Girilecek format:")
print("--Birinci sırada satırdaki sabit katsayı oamalıdır ")
print("--z nin azalan üss değerine göre katsayılar girilmelidir. ")
print("--Eğer sıraya göre o üsste bulunan z değeri yok ise katsayı 0 olarak girilmelidi. .")
print("Örnek girdi;")
print('')
print("2 + 4z^(-1) + 6z^(-2) + 8z^(-3) ")
print("----------------------------------")
print("1 + 3z^(-1) + 5z^(-2) + 7z^(-3) ")
print('')
print("Üst Satırdaki değerleri giriniz:2 4 6 8")
print("Alt Satırdaki değerleri giriniz:1 3 5 7")
print('******************************************************************************************')
ustzkatsayisiras = list(input('Üst Satırdaki değerleri giriniz:').split())
altzkatsayisiras = list(input('Alt Satırdaki değerleri giriniz:').split())
ustz=len(ustzkatsayisiras)-1
altz=len(altzkatsayisiras)-1

ustzkatsayisira = []
altzkatsayisira = []



if altzkatsayisiras[0] == '0':
    print("Alt satir ilk sayı 0 olamaz!!")
    exit()
else:

    for i in range(0, len(ustzkatsayisiras)):
        ustzkatsayisira.append(int(ustzkatsayisiras[i]))

    for i in range(0, len(altzkatsayisiras)):
        altzkatsayisira.append(int(altzkatsayisiras[i])/int(altzkatsayisiras[0]))
    print(altzkatsayisira)
    turtle.screensize(1500,1000)
    t1= turtle.Turtle()
    t2 = turtle.Turtle()

    t1.penup()
    t1.backward(200)
    t1.pendown()
    t2.penup()
    t2.backward(200)
    t2.pendown()

    for i in range(ustz):
        box(t1,False,'z^(-1)')
    circle(t1,3)
    for i in range(altz):
        box(t1,False,'z^(-1)')
    t1.forward(15)



    t2.forward(15)
    t2.color("blue")
    for i in range(len(ustzkatsayisira)):
        if ustzkatsayisira[i] != 0:
            ustCiz(t2,(len(ustzkatsayisira)-i)*50,ustz-i,False,ustzkatsayisira[i])
        elif ustzkatsayisira[i] == 0:
            t2.penup()
            ustCiz(t2,(len(ustzkatsayisira)-i)*50,ustz-i,True,ustzkatsayisira[i])
            t2.pendown()
            pass

    t1.color("red")
    for i in range(len(altzkatsayisira)):
        if altzkatsayisira[len(altzkatsayisira)-(i+1)] != 0:
            altCiz(t1,(len(altzkatsayisira)-i)*50,altz-i,False,altzkatsayisira[len(altzkatsayisira)-(i+1)])
        elif altzkatsayisira[len(altzkatsayisira)-(i+1)] == 0:
            t1.penup()
            altCiz(t1,(len(altzkatsayisira)-i)*50,altz-i,True,altzkatsayisira[len(altzkatsayisira)-(i+1)])
            t1.pendown()

    time.sleep(30)