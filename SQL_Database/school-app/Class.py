class Class():
    def __init__(self,id,name,teacherid):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid
    
    @staticmethod
    def convertClass(obj):
        
        if isinstance(obj,tuple):
            return Class(obj[0],obj[1],obj[2])

        liste = []
        for cl in obj:
            liste.append(Class(cl[0],cl[1],cl[2]))
            pass
        return liste
       