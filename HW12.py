#Name: Max Clark
#Class: 5th Hour
#Assignment: HW12


#1. Print Hello World!

print("Hello World")

#2. Create three different boolean variables named wifi, login, and admin.

wifi = ("F")
login = ("F")
admin = ("F")

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

Times = 0
Attepmts = 0
Begins = ("N")

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

while Begins == ("N"):
    if wifi == ("T"):
        if login == ("T"):
            if admin == ("T"):
                print("Welcome to the program.")
                Times += 1
                Attepmts += 1
                print(f"Entrence times = {Times}. Attaempmts in general = {Attepmts}")
                Begins = input("Do you want to exit? Type Y or N:")
                wifi = ("F")
                login = ("F")
                admin = ("F")
            else:
                print("ERROR! You need to fixs you admin")
                Attepmts += 1
                print(f"Entrence times = {Times}. Attaempmts in general = {Attepmts}")
                admin = input("Please type true or false as T or F for admin:")
        else:
            print("ERROR! You need to fixs you login")
            Attepmts += 1
            print(f"Entrence times = {Times}. Attaempmts in general = {Attepmts}")
            login = input("Please type true or false as T or F for login:")
    else:
        print("ERROR! You need to fixs you wifi")
        Attepmts += 1
        print(f"Entrence times = {Times}. Attaempmts in general = {Attepmts}")
        wifi = input("Please type true or false as T or F for wifi:")

print("Closing program . . .")