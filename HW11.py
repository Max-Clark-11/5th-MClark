#Name: Max Clark
#Class: 5th Hour
#Assignment: HW11

import random
Num1 = False
Num2 = False
Num3 = False

#1. Print "Hello World!"

print("Hello World")

#2. Create a list with three variables that each randomly generate a number between 1 and 100

Num_List = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]

#3. Print the list.

print(Num_List)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if Num_List[0] > Num_List[1] and Num_List[0] > Num_List[2]:
    print(Num_List[0])
    Num1 = True
elif Num_List[1] > Num_List[0] and Num_List[1] > Num_List[2]:
    print(Num_List[1])
    Num2 = True
elif Num_List[2] > Num_List[0] and Num_List[2] > Num_List[1]:
    print(Num_List[2])
    Num3 = True
else:
    print("Some of the numbers above are equal.")

#5. Tie the result (the largest number) from #4 to a variable called "num".

if Num1 == True:
    num = Num_List[0]
elif Num2 == True:
    num = Num_List[1]
else:
    num = Num_List[2]
print(num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by 2 and 3")
    else:
        print(f"{num} is divisible by 2, but not divisible by 3")
elif num % 3 == 0:
    print(f"{num} is divisible by 3, but not divisible by 2")
else:
    print(f"{num} is not divisible by 2 or 3")