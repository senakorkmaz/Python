class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie object created')
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('film silindi')

myList = [1,2,3]

m = Movie('film adi','yonetmen adi',120)

print(str(myList))
print(str(m))
print(len(myList))
print(len(m))
del m
