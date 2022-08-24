import json

filename = 'users.json'

class User:
    def __init__(self, username, password, email, age, phone):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone


class PyRequest():
    def __init__(self, headers=list(), authorization=None, body=dict(), user=None):
        self.headers = headers
        self.authorization = authorization
        self.body = body
        self.user = user

    def local_login(self, username, password):
        with open(filename) as f:
            fd = json.load(f)
            for i in fd:
                if i['username'] == username and i['password'] == password:
                    self.user = User(i['username'], i['password'],
                                     i['email'], i['age'], i['phone'])


def getUserInfo(request):
    if request.user:
        print(request.user.items)


def login():
    username = input("Type yout username: ")
    password = input("Type your password: ")
    request = PyRequest()
    request.local_login(username, password)
    getUserInfo(request)


def reg():
    reg_req = input('Do you want to creat an account(y/n): ')
    if reg_req == 'y':
        username = input('Type your username :')
        password = input('Type your password :')
        email = input('Type your email :')
        age = input('Type your age :')
        phone = input('Type your phone number :')
        data = {
            'username' : username,
            'password' : password,
            'email' : email,
            'age' : age,
            'phone' : phone 
        }
        with open(filename) as f:
            fd = json.load(f)
            fd.append[data]
            json.dump(fd, f, indent=4)

    elif reg_req == 'n':
        pass
    else:
        print("please type valid answer")
        reg()


def Start():
    acc_req = input("Do you have account(y/n): ")
    if acc_req == 'y':
        login()
    elif acc_req == 'n':
        reg()
    else:
        Start()

Start()
