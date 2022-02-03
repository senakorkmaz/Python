from connection import connection
from datetime import datetime

class Student:

    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def addStudent(self):
        sql = 'INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUE (%s,%s,%s,%s,%s)'
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit eklendi.')
            print(f'Son eklenen kaydin id: {Student.mycursor.lastrowid}')
        except connection.connector.Error as err:
            print('Bir hata olustu',err)
        finally:
            Student.connection.close()

    @staticmethod
    def addStudents(students):
        sql = 'INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUE (%s,%s,%s,%s,%s)'
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit eklendi.')
            print(f'Son eklenen kaydin id: {Student.mycursor.lastrowid}')
        except connection.connector.Error as err:
            print('Bir hata olustu',err)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        sql = 'SELECT StudentNumber,Name,Surname FROM student'
        sql = 'SELECT Name,Surname FROM student WHERE Gender="K"'
        sql = 'SELECT * FROM student WHERE YEAR(birthdate)=2003'
        sql = 'SELECT * FROM student WHERE name = "Ali" and YEAR(birthdate)=2005'
        sql = 'SELECT * FROM student WHERE Name like "%An%"  or Surname LIKE "%An%"'
        sql = 'SELECT COUNT(*) FROM student WHERE Gender="K"'
        sql = 'SELECT * FROM student WHERE Gender="K" Order By Name '
        
        Student.mycursor.execute(sql)

        result = Student.mycursor.fetchall()
        for student in result:
            print(student)

    @staticmethod
    def getStudentById(id):
        sql = 'SELECT * FROM student WHERE id=%s '
        value = (id,)
        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(
                obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except Student.connector.Error as err:
            print('Bir hata olustu',err)
        
    @staticmethod
    def updateStudents(list):
        sql='UPDATE student SET studentNumber = %s, name = %s ,surname=%s, birthdate=%s, gender=%s where id=%s'
        values =[]
        order = [1,2,3,4,5,0]

        for item in list:
            item = [item[i] for i in order]
            values.append(item)
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit guncellendi.')
        except Student.connector.Error as err:
            print('Bir hata olustu',err)

    def updateStudent(self):
        sql='UPDATE student SET studentNumber = %s, name = %s ,surname=%s, birthdate=%s, gender=%s where id=%s'
        params = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,params)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit guncellendi.')
        except Student.connector.Error as err:
            print('Bir hata olustu',err)

    @staticmethod
    def getStudentsByGender(gender):
        sql = 'SELECT * FROM student WHERE gender=%s '
        value = (gender,)
        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except Student.connector.Error as err:
            print('Bir hata olustu',err)
        


students = Student.getStudentsByGender('E')
print(students)

# liste = []
# for student in students :
#     student = list(student)
#     student[2]='Mr. ' + student[2]
#     liste.append(student)

# Student.updateStudents(liste)

# students = Student.getStudentsByGender('E')

# for student in students :
#     print(student)

# student = Student.getStudentById(5)

# student.name = 'Mehmet'
# student.surname = 'Halat'

# student.updateStudent()


# Student.StudentInfo()

# student = Student('204','Canan','Tan',datetime(2005,7,17),'K')
# student.addStudent()

# list=[
#      ('301','Ahmet','Yilmaz',datetime(2005,5,17),'E'),
#      ('302','Ali','Can',datetime(2005,6,17),'E'),
#      ('304','Canan','Tan',datetime(2005,7,17),'K'),
#      ('305','Ayse','Taner',datetime(2005,9,17),'K'),
#      ('306','Bahadir','Toksoz',datetime(2004,7,27),'E'),
#      ('307','Ali','Cenk',datetime(2003,8,25),'E')
#  ]
# Student.addStudents(list)


#database ismi vermeden databaselere ulasim
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
#     print(i)