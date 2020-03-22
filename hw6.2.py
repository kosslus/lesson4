def deviders(k):
    tom = []
    for i in range(1, k + 1):
        if k % i == 0:
            tom.append(i)
    return tom


koss = int(input("..."))
print(deviders(koss))
