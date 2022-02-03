class Student():
    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classid):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birtdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def convertStudent(obj):
        
        if isinstance(obj,tuple):
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])

        liste = []
        for student in obj:
            liste.append(Student(student[0],student[1],student[2],student[3],student[4],student[5],student[6]))
            pass
        return liste
