#Max Clark
#5th Hour
#HW6


#1. Create a list with 9 different numbers inside.
Numbers = [7, 40, 3, 2, 67, 700, 5000, 1470, 123]

#2. Sort the list from highest to lowest.
Numbers.sort(reverse=True)

#3. Create an empty list.
List = []

#4. Remove the median number from the first list and add it to the second list.
Removed = Numbers[4]
Numbers.pop(4)
List.append(Removed)

#5. Remove the first number from the first list and add it to the second list.
Removed2 = Numbers[0]
Numbers.pop(0)
List.append(Removed2)

#6. Print both lists.
print(Numbers)
print(List)

#7. Add the two numbers in the second list together and print the result.
Sum = List[0] + List[1]
print(Sum)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Removed = List[0]
Removed2 = List[1]
List.pop(0)
List.pop(0)
Numbers.append(Removed)
Numbers.append(Removed2)

#9. Sort the first list from lowest to highest and print it.
Numbers.sort()
print(Numbers)