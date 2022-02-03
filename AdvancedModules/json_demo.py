import json
import os
from types import new_class

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user : User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanici olusturuldu')

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapildi')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Cikis yapildi.')

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list,file) 
    def identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username}')
        else:
            print('giris yapilmadi')


respository = UserRepository()
while True:
    print('Menu'.center(50,"*"))
    secim = input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeciminiz:')
    if secim == '5':
        break
    else:
        if secim == '1':
           username = input('username:')
           password = input('password:')
           email = input('email:')

           user = User(username=username,password=password,email=email)
           respository.register(user)

           print(respository.users)
        elif secim == '2':
            username = input('username:')
            password = input('password:')
            respository.login(username=username,password=password)

        elif secim == '3':
            respository.logout()
        elif secim == '4':
            respository.identity()
        else: 
            print('yanlis secim')

        
