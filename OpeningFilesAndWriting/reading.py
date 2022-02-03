# try:
#     file = open("newfile22.txt","r")
#     print(file)
# except FileNotFoundError:
#     print('Dosya okuma hatasi')
# finally:
#     print('Dosya kapandi.')
#     file.close()

file = open('newfile.txt',"r",encoding='utf-8')

#for loop
# for i in file:
#     print(i,end='')

#******************** read() fonksiyonu
# content1 = file.read()
# print('icerik1')
# print(content1)

# content2 = file.read()

# print('icerik2')
# print(content2)


# content = file.read(5)
# content = file.read(4)
# print(content)

#*************** readline() fonksiyonu
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')

#******************** readlines() fonksiyonu
liste = file.readlines()
print(liste)

file.close()