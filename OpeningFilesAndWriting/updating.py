'''******Sayfa basindan gincelleme *******'''
#***Var olan bilgiyi siler
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.write("deneme")
#     file.seek(0)
#     print(file.read())

#*****Hic bir bilgiyi silmeden basa ekleme yapip dosyaya yazdirdik
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" + content
#     file.seek(0)
#     file.write(content)


'''*******************Sayfa sonuna ekleme*****************'''
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nSenanur son ekelenen.")


'''*******************Sayfa ortasina ekleme*****************'''
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Ali veli\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())