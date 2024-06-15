# Main objective is to create a program that makes us play the Hangman game, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19140890#overview (Course enrolling is mandatory)


import random


world_list = ["ardvark", "baboon", "camel"]
display = []


chosen_word = random.choice(world_list)
print(f"Purpose for testing: {chosen_word}")


guess = input("Guess a letter: ")
guess = guess.lower()

for letter in chosen_word:
    letter_display = "_"
    display.append(letter_display)


for index in range(0, len(chosen_word)):
    if guess in chosen_word[index]:
        display.pop(index)
        display.insert(index, guess)

print(display)
