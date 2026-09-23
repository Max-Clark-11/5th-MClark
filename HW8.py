#MaxClark
#5th Hour
#HW8


#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hello World")

#3. Create three different variables that each randomly generate an integer between 1 and 10
Int1 = random.randint(1,10)
Int2 = random.randint(1,10)
Int3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(Int1, Int2, Int3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
Int1 = Int1 + 2
Int2 = Int2 - 4
Int3 = Int3 * 1.5
#6. Print each result from #5 on the same line.
print(Int1, Int2, Int3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
Dice_List = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
Dice_List.sort()
print(Dice_List)
#9. Add together the highest three numbers in the list from #7 and print the result.
Highest = Dice_List[3] + Dice_List[4] + Dice_List[5]
print(Highest)
#10. Create a list with 5 names of other students in this class and print the list.
Class = ["Max", "Wyatt", "Cruz", "Echo", "Santi"]
print(Class)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Class)
print(Class)
#12. Print a random choice from the list of names from #10.
print(Class[random.randint(0,4)])