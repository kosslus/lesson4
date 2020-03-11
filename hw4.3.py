import random

log = input("Write your login:")
a = {'login1': ['password', random.randint(0, 100000)],
    'login2': ['password', random.randint(0, 100000)],
    'login3': ['password', random.randint(0, 100000)],
    'login4': ['password', random.randint(0, 100000)],
    'login5': ['password', random.randint(0, 100000)],
    'login6': ['password', random.randint(0, 100000)],
    'login7': ['password', random.randint(0, 100000)],
    'login8': ['password', random.randint(0, 100000)],
    'login9': ['password', random.randint(0, 100000)],
    'login10': ['password', random.randint(0, 100000)],}
if log not in a:
    password=input("Wrong password!!!Generate new password!")
    a.setdefault(log,[password, random.randint(0,100000)])
    print(log)
else:
    password = input(':')#password
    if password in a:
        print(a,[log])
    else:
        print("Wrong!")




