# Main objective is to create a simulation game of Rock, Paper and Scissors game, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/18029131#overview (Course enrolling is mandatory)


# Thanks to @wynand1004 - https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe for the ASCII Code art for the Rock, Paper and Scissors shapes


import random



# Rock
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


choice_user = int(input("What do you want to choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice_user == 0:
    print(rock)
elif choice_user == 1:
    print(paper)
elif choice_user == 2:
    print(scissors)
else:
    print("There are no other options.")

choice_machine = random.randint(0,2)
if choice_machine == 0:
    print(f"\nComputer Choice: \n{rock}")
elif choice_machine == 1:
    print(f"\nComputer Choice: \n{paper}")
else:
    print(f"\nComputer Choice: \n{scissors}")

# Interpretation of Wins or Loss :

if choice_user == choice_machine :
    print("No one wins. Restart again !")
else:
    if (choice_user == 0 and choice_machine == 1) or (choice_user == 1 and choice_machine == 2) or (choice_user == 2 and choice_machine == 0):
        print("You lose.")
    else:
        print("You win.")

