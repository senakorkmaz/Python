# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open(dosya_adi,dosya_erisme_modu)
# dosya_erisme_modu => dosyayi hangi amacla actigimizi belirtir.

# "w": (Write) yazma modu. Dosyayi konumda olustutur.
# ** mevcutta bir bilgi varsa siler
#file = open('newfile.txt','w')
#file.close()

#file = open("C:/users/senak/desktop/newfile.txt","w")
#file = open('newfile.txt','w',encoding='utf-8')
#file.write('Senanur KORKMAZ ')
#file.close()


# "a": (Append) ekleme. Dosya konumda yoksa olusturur.
#file = open("newfile.txt","a",encoding="utf-8")
#file.write('\nsenanur korkmaz')
#file.close()



# "x": (Create) olusturma. Dosya zaten varsa hata verir.
#Sadece olusturur
file = open("newfile2.txt","x",encoding="utf-8")
# "r": (Read) okuma. Dosya konumda yoksa hata verir.