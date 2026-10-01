#Name: Max Clark
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

Enemies = {
    "Blob" : {
        "Hp" : 10,
        "Attack" : 2,
        "Defense" : 0,
        "Type" : "very weak"
    },
    "Big Blob" : {
        "Hp" : 20,
        "Attack" : 3,
        "Defense" : 0,
        "Type" : "normal"
    },
    "Zombie" : {
        "Hp" : 7,
        "Attack" : 3,
        "Defense" : 5,
        "Type" : "weak"
    },
    "Bones": {
        "Hp": 15,
        "Attack": 5,
        "Defense": 2,
        "Type": "strong"
    },
    "Grave Stone Boss": {
        "Hp": 50,
        "Attack": 10,
        "Defense": 5,
        "Type": "very strong"
    },
}
print("Blob :", Enemies["Blob"])
print("Big Blob :", Enemies["Big Blob"])
print("Zombie :", Enemies["Zombie"])
print("Bones :", Enemies["Bones"])
print("Grave Stone Boss :", Enemies["Grave Stone Boss"])

#Logic to change stats
Starting = input("Do you want to change the stats? Remember to only use capital letters when needed. :")
if Starting == "yes" :
    Enemy = input("Which enemy? :")
    Stat = input("Which stat? :")
    Amount = input("Add vaules or words.")
#Blob
    if Enemy == "Blob":
        if Stat == "Hp":
            Enemies["Blob"].update({"Hp" : Amount})
        if Stat == "Attack":
            Enemies["Blob"].update({"Attack" : Amount})
        if Stat == "Defense":
            Enemies["Blob"].update({"Defense": Amount})
        if Stat == "Type":
            Enemies["Blob"].update({"Type" : Amount})
#Big Blob
    if Enemy == "Big Blob":
        if Stat == "Hp":
            Enemies["Big Blob"].update({"Hp" : Amount})
        if Stat == "Attack":
            Enemies["Big Blob"].update({"Attack" : Amount})
        if Stat == "Defense":
            Enemies["Big Blob"].update({"Defense": Amount})
        if Stat == "Type":
            Enemies["Big Blob"].update({"Type" : Amount})
# Zombie
    if Enemy == "Zombie":
        if Stat == "Hp":
            Enemies["Zombie"].update({"Hp": Amount})
        if Stat == "Attack":
            Enemies["Zombie"].update({"Attack": Amount})
        if Stat == "Defense":
            Enemies["Zombie"].update({"Defense": Amount})
        if Stat == "Type":
            Enemies["Zombie"].update({"Type": Amount})
# Bones
    if Enemy == "Bones":
        if Stat == "Hp":
            Enemies["Bones"].update({"Hp": Amount})
        if Stat == "Attack":
            Enemies["Bones"].update({"Attack": Amount})
        if Stat == "Defense":
            Enemies["Bones"].update({"Defense": Amount})
        if Stat == "Type":
            Enemies["Bones"].update({"Type": Amount})
# Grave Stone Boss
    if Enemy == "Grave Stone Boss":
        if Stat == "Hp":
            Enemies["Grave Stone Boss"].update({"Hp": Amount})
        if Stat == "Attack":
            Enemies["Grave Stone Boss"].update({"Attack": Amount})
        if Stat == "Defense":
            Enemies["Grave Stone Boss"].update({"Defense": Amount})
        if Stat == "Type":
            Enemies["Grave Stone Boss"].update({"Type": Amount})



    print("Blob :", Enemies["Blob"])
    print("Big Blob :", Enemies["Big Blob"])
    print("Zombie :", Enemies["Zombie"])
    print("Bones :", Enemies["Bones"])
    print("Grave Stone Boss :", Enemies["Grave Stone Boss"])
else :
    print("Pretending to save all your progress")









