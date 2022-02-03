from dbmanager import DbManager
from Student import Student
class App:
    def __init__(self,):
        self.db = DbManager()

    def initApp(self):
        msg='*****\n1-Ogrenci Listesi\n2-Ogrenci Ekle\n3-Ogrenci Guncelle\n4-Ogrenci Sil\n5-Ogretmen Ekle\n6-Siniflara gore Dersler\n7-Cikis(E/C)'
        while True:
            print(msg)
            islem = input('Secim: ')

            if islem == '1':
                self.getStudents()
            elif islem == '2':
                student = self.db.getStudentById(5)
                student.studentNumber = int(input('Ogrenci Numarasi Giriniz: '))
                student.name = input('Isim giriniz: ')
                student.surname = input('Soyad giriniz: ')
                student.gender = input('Cinsiyet giriniz(E/K): ')
                self.classPrint()
                student.classid= int(input('Sinif Id giriniz:'))
                self.db.addStudent(student)
                print('======Yeni Sinif Listesi======')
                self.studentPrint(student.classid)
                pass
            elif islem == '3':
                self.getStudents()
                id = input('Guncellenecek ogrenci Id:')
                student = self.db.getStudentById(id)
                student.name = input('Yeni isim giriniz: ')
                student.surname = input('Yeni soyad giriniz: ')
                self.db.editStudent(student)
                pass
            elif islem == '4':
                self.getStudents()
                id = int(input('Silinecek ogrenci Id:'))
                student = self.db.getStudentById(id)
                self.db.deleteStudent(student)
                pass
            elif islem == '5':
                pass
            elif islem == '6':
                pass
            elif islem == '7':
                pass
            elif islem == 'E' or islem=='C':
                break
            else:
                print('Yanlis secim')

    def getStudents(self):
            self.classPrint()
            id = int(input('Sinif Id giriniz:'))
            self.studentPrint(id)

    def classPrint(self):
            listClass = self.db.getClass()
            for i in listClass:
                print('Sinif Id',str(i.id).ljust(5,' '),'Sinif',i.name)

    def studentPrint(self,id):
            list = self.db.getStudentsByClassId(id)
            for student in list:
                print('Id: ',str(student.id).ljust(4,' '),'Name: ',student.name.ljust(14,' '),'  Surname: ',student.surname)

app = App()

app.initApp()