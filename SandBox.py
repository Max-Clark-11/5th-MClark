#RPG
import random

#Variables
Level = 1
HPplus = 0
MPplus = 0
Aplus = 0
Dplus = 0
MaxHP = 18 + (Level * 2) + HPplus
MaxMP = 4 + Level + MPplus
HP = MaxHP
MP = MaxMP
A = 0.5 + (Level / 2) + Aplus
D = 0.5 + (Level / 2) + Dplus
EXP = 0
Coins = 0
Gamespot = 1
MoveAttack = False
MoveDefend = False
MoveCharge = False
MoveHeal = False
MoveRun = False
MoveDiceCharge = False
MoveBombs = False
Bombs = 0
Game = 1
Fighting = False
Losing = False
Fight = 1
Turn = 1
Nothing = 0
Coins = 0
EXP = 0
EvilPeopleKilled = 0
EffectD = D
EffectA = A
OutsideBarFight = False
BeerTenderFight = False
DoorBroken = False
EvilPersonKilled1 = False
#Before Game
print("Hello! Welcome to the game. You will be able to use ablilities on yourscreen. If you need to choose something, pick a number for it.")
Name = input("Enter your name:")
MoveAttack = True
MoveDefend = True
#Main areas
while Game == 1:
    if Fighting == False:
        if Gamespot == 1:
            Choices = int(input("You arrive in a town. Do you want to go to the bar, the shop, a random house, or leave the town? :"))
#Bar stuff
            if Choices == 1:
                if OutsideBarFight == False:
                    if Choices == 1:
                        Choices = 0
                        Choices = input("You are about to enter a bar, and you see a blob attacking an person on the side of the bar. Do you help them? :")
                        Gamespot = 2
                else:
                    Gamespot = 4

        if Gamespot == 2:
            if Choices == "1":
                EHP = 4
                EMP = 5
                EAttack = 3
                EDefend = 0
                Turn = 1
                Fighting = True
                Enemy = 1

            if Choices == "2":
                Gamespot = 4

        if Gamespot == 3:
            print("Person - 'Thank you for saving me. I can pay you back with information.'")
            print("Person - 'In the bar, always bet on how many people are playing plus 3 to have the best odds.'")
            OutsideBarFight = True
            Gamespot = 4

        if Gamespot == 4:
            Choices = int(input("You are in the bar. Do you go to the counter, go to the gambaling table, talk to people, or leave? :"))
            if Choices == 1:
                Gamespot = 7
                Choices = 0
            if Choices == 2:
                Gamespot = 14
                Choices = 0
            if Choices == 4:
                Gamespot = 1
                Choices = 0

        if Gamespot == 7:
            print("Bar Tender - 'Welcome. What Can I do for you?'")
            Choices = int(input("Nothing, Do you have a Job?:"))
            if Choices == 1:
                print("Bar Tender - 'Oh.'")
                Gamespot = 4
                Choices = 0
            if Choices == 2:
                if BeerTenderFight == False:
                    print("Bar Tender - 'So you are the new guys. Go around back and tenderize the Beer. Don't Ask.'")
                    EHP = 2
                    EMP = 5
                    EAttack = 4
                    EDefend = 1
                    Turn = 1
                    Fighting = True
                    Enemy = 2
                    Choices = 0
                    BeerTenderFight = True
                else:
                    print("Bar Tender - 'I don't have anything you need to do.'")

        if Gamespot == 8:
            print("Bar Tender - 'Great job! Here's a few coins for your work.'")
            Coins += 5
            print("You got 5 coins!")
            Gamespot = 4

        if Gamespot == 14:
            People = random.randint(2, 5)
            if Coins <= 0:
                print("You need money to make money.")
                Gamespot = 4
            else:
                print(f"There are {People} people at the table.")
                print(f"You have {Coins} coins")
                MoneyBet = int(input("How many coins do you want to bet? :"))
                if Coins < MoneyBet:
                    print("The other players get mad at you because you don't have that many coins.")
                else:
                    GameBet = int(input("From 1 - 10, what do you want to bet on? :"))
                    if 0 < GameBet < 11:
                        if GameBet == People + 3:
                            Random = random.randint(1,2)
                            if Random >= 2:
                                Gained = MoneyBet * 2
                                Coins += Gained
                                print(f"You gained {Gained} coins")
                                print(f"You have {Coins} coins")
                                Choices = int(input("Do you want to keep gambiling, or do you want to leave? :"))
                                if Choices == 1:
                                    print("You go to another table")
                                else:
                                    Gamespot = 4
                            else:
                                print("You lose")
                                Coins -= MoneyBet
                                print(f"You have {Coins} coins")
                                Choices = int(input("Do you want to keep gambiling, or do you want to leave? :"))
                                if Choices == 1:
                                    print("You go to another table")
                        else:
                            Random = random.randint(1,10)
                            if Random <= 1:
                                Gained = MoneyBet * 2
                                Coins += Gained
                                print(f"You gained {Gained} coins")
                                print(f"You have {Coins} coins")
                                Choices = int(input("Do you want to keep gambiling, or do you want to leave? :"))
                                if Choices == 1:
                                    print("You go to another table")
                                else:
                                    Gamespot = 4
                            else:
                                print("You lose")
                                Coins -= MoneyBet
                                print(f"You have {Coins} coins")
                                Choices = int(input("Do you want to keep gambiling, or do you want to leave? :"))
                                if Choices == 1:
                                    print("You go to another table")
                    else:
                        print("Your skipped because it has to be between 1 and 10.")


#Shop 1 stuff
        if Gamespot == 1:
            if Choices == 2:
                Gamespot = 5
                Choices = 0

        while Gamespot == 5:
            print(f"You have {Coins} Coins.")
            Choices = int(input("HPplus: 2 (1), MPplus: 3 (2), Aplus: 7 (3), Dplus: 5 (4), 5 Bombs: 4 (5), Leave (6)"))
            if Choices == 1:
                if Coins >= 2:
                    Coins -= 2
                    HPplus += 1
                    MaxHP = 10 * (Level * 2) + HPplus
                    HP = MaxHP
                    print("You got a Health Points Plus.")
                else:
                    print("Not enough coins.")

            if Choices == 2:
                if Coins >= 3:
                    Coins -= 3
                    MPplus += 1
                    MaxMP = 5 * Level + MPplus
                    MP = MaxMP
                    print("You got a Magic Points Plus.")
                else:
                    print("Not enough coins.")

            if Choices == 3:
                if Coins >= 7:
                    Coins -= 7
                    Aplus += 1
                    A = 2 * (Level / 2) + Aplus
                    EffectA = A
                    print("You got an Attack Plus.")
                else:
                    print("Not enough coins.")

            if Choices == 4:
                if Coins >= 5:
                    Coins -= 5
                    Dplus += 1
                    D = 2 * (Level / 2) + Dplus
                    EffectD = D
                    print("You got a Defend Plus.")
                else:
                    print("Not enough coins.")

            if Choices == 5:
                if Coins >= 4:
                    Coins -= 4
                    Bombs += 5
                    print("You got five bombs.")
                else:
                    print("Not enough coins.")

            if Choices == 6:
                Gamespot = 1
                Choices = 0

#Random House 1
        if Gamespot == 1:
            if Choices == 3:
                Gamespot = 9
        if Gamespot == 9:
            if DoorBroken == False:
                Choices = int(input("You are a the house. Do you knock on the door, or break in? :"))
                if Choices == 1:
                    print("No one answered.")
                if Choices == 2:
                    EHP = 3
                    EMP = 0
                    EAttack = 1
                    EDefend = 0
                    Turn = 1
                    Fighting = True
                    Enemy = 3
                    Choices = 0
                    DoorBroken = True

            else:
                Gamespot = 10

        if Gamespot == 10:
            Choices = int(input("You are in the entre way. Do you go left to the stair case, forward to the kichent, or right to the hallway? :"))
            if Choices == 1:
                Gamespot = 11
                Choices = 0

        if Gamespot == 11:
            Choices = int(input("You are in the upstairs hallway. Do you enter the room or leave back to town? :"))
            if Choices == 1:
                Gamespot = 12
                Choices = 0
            if Choices == 2:
                Gamespot = 1
                Choices = 0

        if Gamespot == 12:
            if EvilPersonKilled1 == False:
                print("You see a dead body with a guy in a black mask standing over him.")
                EHP = 10
                EMP = 6
                EAttack = 2
                EDefend = 0
                Turn = 2
                Fighting = True
                Enemy = 4
                Choices = 0
                EvilPersonKilled1 = True

            else:
                print("There's nothing here")
                Gamespot = 10

        if Gamespot == 13:
            print("The man escapes out a window. He runs out of the town. He left a bomb bag and five bombs.")
            MoveBombs = True
            Bombs += 5
            EvilPeopleKilled += 1
            Gamespot = 1

#Outside the town
        if Gamespot == 1:
            if Choices == 4:
                Gamespot = 6

        if Gamespot == 6:
            Choices = int(input("You exit the town. Do you want to stick to the path, or go off trail? :"))

#the fight

    while Fighting == True:

#your turn
        if Turn == 1:
            print("HP:" + str(EHP) , "MP:" + str(EMP) , "Attack:" + str(EAttack) , "Defend:" + str(EDefend))
            print()
            print("HP:" + str(HP), "MP:" + str(MP), "Attack:" + str(A), "Defend:" + str(D))
            print()
            if MoveAttack == True:
                print("Attack:0  (1)")
            if MoveDefend == True:
                print("Wait:0  (2)")
            if MoveDefend == True:
                print("Defend:1  (3)")
            if MoveCharge == True:
                print("Charge:1  (4)")
            if MoveDiceCharge == True:
                print("DiceCharge:1  (5)")
            if MoveBombs == True:
                print(f"MoveBombs (6) Bombs:{Bombs}")
            Move = int(input("Choose a move:"))

            if Move == 1:
                Dice = random.randint(1,6)
                if Dice <= 3:
                    print("you got a" , str(Dice))
                    print(str(Name) , "missed")
                    if EffectA == A:
                        Nothing = 0
                    else:
                        A = EffectA
                    Turn = 2
                else:
                    print("You got a" , str(Dice))
                    print(str(Name) , "hit the enemy")
                    EHP -= A - EDefend
                    if EffectA == A:
                        nothing = 0
                    else:
                        A = EffectA
                    Turn = 2

            if Move == 2:
                print(str(Name), "waited")
                Turn = 2

            if Move == 3:
                if MP >= 1:
                    EffectD = D
                    D = D * 2
                    print(str(Name) , "defended")
                    MP = MP - 1
                    Turn = 2
                else:
                    print(str(Name), "did nothing")
                    Turn = 2

            if MoveCharge == True:
                if Move == 4:
                    if MP >= 1:
                        EffectA = A
                        A = A * 2
                        print(str(Name) , "charged")
                        MP = MP - 1
                        Turn = 2
                    else:
                        print(str(Name), "did nothing")
                        Turn = 2

            if MoveBombs == True:
                if Move == 6:
                    if Bombs >= 1:
                        EHP -= 2 * A - EDefend
                        if EffectA == A:
                            nothing = 0
                        else:
                            A = EffectA
                        print(str(Name) , "bombed the enemy")
                        Bombs -= 1
                        Turn = 2
                    else:
                        print(str(Name), "did nothing")
                        Turn = 2

        if HP <= 0:
            Losing = True
            while Losing == True:
                print("You lose!")

        if EHP <= 0:
            print("You win!")
            if EffectD == D:
                nothing = 0
            else:
                D = EffectD
            if EffectA == A:
                nothing = 0
            else:
                A = EffectA
            if Enemy == 1:
                Random = random.randint(1, 3)
                EXP = EXP + Random
                print("You gained", str(Random), "EXP")
                Random = random.randint(1,3)
                Coins = Coins + Random
                print("You gained", str(Random), "coins")
                Fighting = False
                Gamespot += 1

            if Enemy == 2:
                Fighting = False
                Gamespot += 1

            if Enemy == 3:
                Random = random.randint(3, 4)
                EXP = EXP + Random
                print("You gained", str(Random), "EXP")
                Fighting = False
                Gamespot += 1

            if Enemy == 4:
                Random = random.randint(4, 6)
                EXP = EXP + Random
                print("You gained", str(Random), "EXP")
                Random = random.randint(2,4)
                Coins = Coins + Random
                print("You gained", str(Random), "coins")
                Fighting = False
                Gamespot += 1

            EXPLevel = Level * 10
            if EXP >= EXPLevel:
                EXP -= EXPLevel
                MaxHP = 10 * (Level * 2) + HPplus
                MaxMP = 5 * Level + MPplus
                HP = MaxHP
                MP = MaxMP
                A = 2 * (Level / 2) + Aplus
                D = 2 * (Level / 2) + Dplus


#enemy's turn
        if Fighting == True:
            if Turn == 2:
                if Enemy == 3:
                    if Move == 1:
                        if Dice <= 3:
                            print(f"{Dice}")
                            print(str(Name) , "hit themselves")
                            Hit = A / 2
                            while Hit > 0:
                                Hit -= 1
                                HP -= 1

                Random = random.randint(1,10)
                Dice = random.randint(1, 6)
                print("The enemy got a" , str(Dice))

                if Enemy == 1:
                    if Dice <= 3:
                        print("The enemy missed")
                        Turn = 1
                    else:
                        print("The enemy hit")
                        Hit = EAttack - D
                        while Hit > 0:
                            Hit -= 1
                            HP -= 1
                        Turn = 1

                if Enemy == 2:
                    if Dice <= 4:
                        print("The enemy missed")
                        Turn = 1
                    else:
                        print("The enemy hit")
                        Hit = EAttack - D
                        while Hit > 0:
                            Hit -= 1
                            HP -= 1
                        Turn = 1

                if Enemy == 4:
                    if Random >= 6:
                        if Dice <= 3:
                            print("The enemy missed")
                            Turn = 1
                        else:
                            print("The enemy hit")
                            Hit = EAttack - D
                            while Hit > 0:
                                Hit -= 1
                                HP -= 1
                            Turn = 1
                    if Random < 6:
                        if EMP >= 2:
                            EMP -= 2
                            if Dice <= 3:
                                print("The enemy missed heavily")
                                Turn = 1
                            else:
                                print("The enemy hit heavily")
                                Hit = EAttack * 2 - D
                                while Hit > 0:
                                    Hit -= 1
                                    HP -= 1
                                Turn = 1
                        else:
                            EMP =+ 3

                Turn = 1

#status
        if EffectD == D:
            nothing = 0
        else:
            D = EffectD