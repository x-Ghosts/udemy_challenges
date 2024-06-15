# Main objective is to create a program that makes us play the Hangman game, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19140890#overview (Course enrolling is mandatory)


import random


world_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(world_list)


guess = input("Guess a letter: ")
guess = guess.lower()

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')