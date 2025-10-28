print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
if cross_road=="right":
    print("The game is over")
if cross_road=="left":
    lake=input("Now you have come across a lake would you like to 'swim' or 'wait' for a baot to arrive ")
    if lake=="swim":
        print("Opps you have been bitten by SLuttyWhale and have been swallowed")
        print("You lost the game")
    if lake=="wait":
        print("The Boat has arrived with on deck captain Sir Mutee")
        print("You have been carefully escorted to an island called iLand")
        house=input("Would you like to hire a 'guide' on the the island to reach the house or use 'google maps' ")
        if house=="google maps":
            print("Your in the middle of nowhere dummy, there's no internet here")
            print("Didn't the hot captain tell you that earlier")
        if house=="guide":
            print("You have now reached the house,This is the final step to find the TREASURE ")
            print("You have 3 doors of each color in front of you, carefully pick the right door or you loose(hint i like blue)")
            door=input("Open the 'blue' door or 'red door' or 'brown' door")
            if door=="blue":
                         print("HURAAAY , YOU HAVE FOUND THE TREASURE,how did you know it was the blue color smartpanst?!")
            if door=="red":
                        print("You have been forcefully involved in an orgy full of anacondas")
            elif door=="brown":
                        print("You fell into a ditch that led you out of the island" )


