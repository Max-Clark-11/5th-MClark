#Name: Max Clark
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!

print("Hello World!")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.

Dictionary = {
    "Hp" : 60,
    "Damage" : [4,5,6],
    "Name" : "Bob"
}

#3. Print the keys of the dictionary from #2.

print(Dictionary.keys())

#4. Print the values of the dictionary from #2

print(Dictionary.values())

#5. Print one of the three numbers from the list by itself

print(Dictionary["Damage"][2])

#6. Using the update function, add a fourth key to the dictionary and give it a value.

Dictionary.update({"Defence" : 1})

#7. Print the entire dictionary from #2 with the updated key and value.

print(Dictionary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

Class_Mates = {
    "Student1" : {
        "Name" : "Wyatt",
        "Grade" : 9,
        "Table_Color" : "Light_Brown"
    },
    "Student2" : {
        "Name" : "Sante",
        "Grade" : 9,
        "Table_Color" : "Black"
    },
    "Student3": {
        "Name": "Cruz",
        "Grade": 9,
        "Table_Color": "Dark_Brown"
    },
}

#9. Print the names of all three classmates on the same line.

print(Class_Mates["Student1"]["Name"], Class_Mates["Student2"]["Name"], Class_Mates["Student3"]["Name"], )

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Class_Mates.pop("Student1")
print(Class_Mates)