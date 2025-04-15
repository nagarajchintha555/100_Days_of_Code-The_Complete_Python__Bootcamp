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

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))

if my_choice>=0 and my_choice<3:
    print(game_images[my_choice])
else:
    print("That's a wrong choice! you lose :(")

random_number = random.randint(0,2)
if my_choice>=0 and my_choice<3:
    print(f"{random_number}")
    print("Computer chose:")
    print(game_images[random_number])
if my_choice==0 and random_number == 0:
    print("Tie!")
elif my_choice==0 and random_number == 1:
    print("You lose!")
elif my_choice==0 and random_number == 2:
    print("You Win!!")
elif my_choice==1 and random_number == 0:
    print("You win!!")
elif my_choice==1 and random_number == 1:
    print("Tie!")
elif my_choice==1 and random_number == 2:
    print("You lose!")
elif my_choice==2 and random_number == 0:
    print("You lose!")
elif my_choice==2 and random_number == 1:
    print("You Win!!")
elif my_choice==2 and random_number == 2:
    print("Tie!")
