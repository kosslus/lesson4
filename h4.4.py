import os

main_dict = {
    'bticket': {33, 76,93, 27, 36, 16},  #basic ticket
    'bticket2': {31, 98, 43, 65, 83, 42},
}

main_list = {
    'premiumticket': [777, 666, 222],
    'premiumticket2': [555, 555, ],
}

choice = None

while True:

    if choice == None:
        print("""
            PLAY AND WIN!
    1.I win take my million
    2.Buy ticket
    
            """)
        choice = input()

    if choice == "1":
        print("""
              You win?
              1. Yes
              2. No!
              """)
        choice += input()

    elif choice == "2":
        print("""
              How to play
              1. Buy basic ticket
              2. Buy premium ticket
              """)
        choice += input()

    if choice == "11":

        print("THANKS FOR YOUR MONEY!!!STUPID!!!")
        print("THIS IS TRICK")

    elif choice == "12":

        print("Try again")

    elif choice == "21":

        name = input('Your ticket number: ')

        main_dict.setdefault(name, {})


    elif choice == "22":

        print(main_dict)
        print(main_list)




