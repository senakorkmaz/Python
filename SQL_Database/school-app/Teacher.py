class Teacher():
    def __init__(self,id,branch,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birtdate = birthdate
        self.gender = gender
       