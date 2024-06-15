# Main objective is to create a program that makes us play the Hangman game, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19140890#overview (Course enrolling is mandatory)


import random


world_list = ["ardvark", "baboon", "camel"]
display = []
blank = "_"


chosen_word = random.choice(world_list)
print(f"Purpose for testing: {chosen_word}")



for letter in chosen_word:
    letter_display = "_"
    display.append(letter_display)


while blank in display:
    letter_entry = input("Guess a letter: ")
    letter_entry = letter_entry.lower()
    for index in range(0, len(chosen_word)):
        if letter_entry in chosen_word[index]:
            display.pop(index)
            display.insert(index, letter_entry)
    print(display)

print("You win.")
