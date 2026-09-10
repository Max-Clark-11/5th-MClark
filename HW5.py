#Max Clark
#5th Hour
#HW5

#1. Print Hello World!
print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.
Names = ["Bob", "Jeff", "Alvin", "Fred", "Kevin"]

#2. Append a new name onto the Name List.
Names.append("Calvin")

#3. Print out the 4th name on the list.
print(Names[3])

#4. Create a list with 4 different integers in it.
Integers = [17, 9, 64, 40]

#5. Insert a new integer into the 2nd spot and print the new list.
Integers.insert(1, 7)
print(Integers)

#6. Sort the list from lowest to highest and print the sorted list.
Integers.sort()
print(Integers)

#7. Add the 1st three numbers on the sorted list together and print the sum.
IntegerSum =Integers[0] + Integers[1] + Integers[2]
print(IntegerSum)

#8. Create a list with two strings, two variables, and too boolean values.
MixList = [7, "Bob", True, 40, "Fred", False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
Asking = int(input("Enter a integer between 1 and 6"))
print(MixList[Asking - 1])