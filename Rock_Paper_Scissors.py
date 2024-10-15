import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

c1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
print(game_images[c1])

c2 = int() 
c2 = random.randint(0,2)
print(game_images[c2])

if (c1 < 0 or c2 >= 3):
    print("You chose an invalid number, You lose!") 

elif (c1 == 0 and c2 == 2):
    print("You win") 

elif(c1 == 2 and c2 == 0):
    print("You lose")

elif (c2 > c1):
    print("You lose") 

elif (c1 > c2): 
    print("You win")

elif(c1 == c2):
    print("It's a draw")