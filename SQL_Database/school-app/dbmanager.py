import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager():

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def closeDb(self):
        self.connection.close()
        print('db kapandi')

    def getStudentById(self,id):
        sql = 'SELECT * FROM student WHERE id=%s'
        value = (id,)

        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.convertStudent(obj)
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)
    
    def getStudents(self):
        sql = 'SELECT * FROM student '

        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Student.convertStudent(obj)
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)
    
    def getStudentsByClassId(self,id):
        sql = 'SELECT * FROM student WHERE classid=%s'
        value = (id,)

        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.convertStudent(obj)
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)

    def addStudent(self,student: Student):
        sql = 'INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUE (%s,%s,%s,%s,%s,%s)'
        value = (student.studentNumber,student.name,student.surname,student.birtdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayit eklendi.')
            print(f'Son eklenen kaydin id: {self.cursor.lastrowid}')
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)

    def editStudent(self,student: Student):
        sql='UPDATE student SET studentNumber = %s, name = %s ,surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s'
        value = (
            student.studentNumber,
            student.name,
            student.surname,
            student.birtdate,
            student.gender,
            student.classid,
            student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayit guncellendi.')
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)

    def deleteStudent(self,student: Student):
        sql = 'DELETE FROM student WHERE id=%s'
        value = (student.id,)

        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayit silindi.')
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)
        pass

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass

    def deleteTeacher(self,teacher: Teacher):
        pass

    def getClass(self):
        sql = 'SELECT * FROM class '

        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.convertClass(obj)
        except mysql.connector.Error as err:
            print('Bir hata olustu',err)



# db = DbManager()

#------------------GET STUDENT---------------
# student = db.getStudentById(6)

# print(student.name)
# print(student.surname)


#-------------GET STUDENTS BY CLASSID---------
# students = db.getStudentsByClassId(1)

# for std in students:
#     print(std.name+' '+std.surname)


#------------ADD STUDENT-------------------
# student = db.getStudentById(5)

# student.name = 'Mehmet'
# student.surname = 'soylu'
# student.studentNumber = '401'
# student.classid = 2

# db.addStudent(student)


#------------UPDATE STUDENT-------------------

# student = db.getStudentById(5)
# student.classid = 2
# db.editStudent(student)
# db.closeDb()