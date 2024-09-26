print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island \nYour mission is to find the treasure.")
print("You have arrived at a Cross-Road. Where do you want to go? Type 'left' or 'right' : ")
pos = str(input()).lower()
if pos == "left":
    print("You have arrived at a lake. There is an island in the middle of the lake.")
    decision = str(input("Type 'wait' to wait for a boat or 'swim' to swim across: ")).lower()
    if decision == "wait":
        print("You have safely reached the island.")
        print("There's a house with 3 doors. One red, another Yellow and the 3rd is Blue.")
        color = str(input("Which color do you choose?")).lower()
        if color == "red":
            print("It's a room full of fire. \nGame Over.")
        elif color == "yellow":
            print("It's room filled with poisonous gas. You died due to poison. \nGame Over.")
        elif color == "blue":
            print("You have found the treasure! You win!")
        else:
            print("Select a correct room.")
    else:
        print("You have chosen to swim. There are aquatic animals in the lake which can harm you.")
        print("Type 'Y' to swim across else 'N' to find for a solution.")
        decision = str(input("Type 'Y' to swim across or 'N' to search for other methods: ")).lower()
        if decision == "Yes" or "yes" or "y" or "Y":
            print("You were eaten by a Shark. Game Over")
        else:
            print("There is a Hot air balloon present")
            decision = str(input("Type 'H' to use or 'S' to swim otherwise.")).lower()
            if decision == 'h' or 'H':
                print("You have arrived on the island.")
                print("There's a house with 3 doors. One red, another Yellow and the 3rd is Blue.")
                color = str(input("Which color do you choose?")).lower()
                if color == "red":
                    print("It's a room full of fire. \nGame Over.")
                elif color == "yellow":
                    print("It's room filled with poisonous gas. You died due to poison. \nGame Over.")
                elif color == "blue":
                    print("You have found the treasure! You win!")
                else:
                    print("Select a correct room.")
            else:
                print("You were eaten by a Shark. Game Over")            
else:
    print("Wrong decision. No road ahead. Game Over")