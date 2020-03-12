import random

log = input('Your login: ')

a = {
    'login0': ['password', random.randint(0, 10000)],
    'login1': ['password', random.randint(0, 10000)],
    'login2': ['password', random.randint(0, 10000)],
    'login3': ['password', random.randint(0, 10000)],
    'login4': ['password', random.randint(0, 10000)],
    'login5': ['password', random.randint(0, 10000)],
    'login6': ['password', random.randint(0, 10000)],
    'login7': ['password', random.randint(0, 10000)],
    'login8': ['password', random.randint(0, 10000)],
    'login9': ['password', random.randint(0, 10000)],
}

if log not in a:

    password = input(' Wrong! Generate new: ')
    a.setdefault(log, [password, random.randint(0, 10000)])#?

    print('New', log)

else:

    password = input('Your password: ')

    if password == a[log][0]:
        print(a[log][1])
    else:
        print('Wrong!')


