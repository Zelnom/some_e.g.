import random

print("Welcome to our game of rock, paper and scissors!")
print("Let's see who has the better hand and better luck")
choice = int(input("What your choice shall be? Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

random_choice = random.randint(0,2)
list_options = [rock, paper, scissors]
calculator_choice = list_options[random_choice]

if choice == 0 or choice == 1 or choice == 2:
    my_choice = list_options[choice]
    if choice == 0 and random_choice == 2:
        print(f"You have chosen {my_choice}\nThe computer chose {calculator_choice}\nYou won!")
    elif choice == 1 and random_choice == 0:
        print(f"You have chosen {my_choice}\nThe computer chose {calculator_choice}\nYou won!")
    elif choice == 2 and random_choice == 1:
        print(f"You have chosen {my_choice}\nThe computer chose {calculator_choice}\nYou won!")
    elif choice == random_choice:
        print(f"You have chosen {my_choice}\nThe computer chose {calculator_choice}\nYou won!")

    else:
        print(f"You have chosen {my_choice}\nThe computer chose {calculator_choice}\nYou lost!")

else:
    print("Please try a valid value!")