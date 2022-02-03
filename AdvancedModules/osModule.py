import os

dirOs = dir(os)
print(dirOs)

osName = os.name
print(osName)

#Dosya konum degistirme
#os.chdir("C:\\")
# os.chdir("..")
# os.chdir("..")

#dosya konum gosterme
#getcwdOs = os.getcwd()
# print(getcwdOs)

#dizin olusturma
#os.mkdir("newdirectory")
#os.makedirs('newdirectory/yenidizin')
#os.rename('newdirectory','olddirectory')
#os.rmdir('deleteddirectory')

#listeleme
#listOs = os.listdir()
#print(listOs)
# listOs = os.listdir(os.chdir(".."))
# print(listOs)
#for dosya in listOs:
#    if dosya.endswith('.py'):
#        print(dosya)

#os.system("notepad.exe")

#path
