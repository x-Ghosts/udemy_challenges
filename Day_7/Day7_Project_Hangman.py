# Main objective is to create a program that makes us play the Hangman game, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/19140890#overview (Course enrolling is mandatory)


import random
import words_list
from words_list import words
from stages import stages, logo


word_list = words_list.words
display = []
previous_guesses = [] #this to track previous user guesses

# Random word choice from the machine.
chosen_word = random.choice(word_list)
print(chosen_word)


for letter in chosen_word:
    display.append("_")


# Check the identity match of the letter chosen within the word randomly picked
def game_process(lifes):
    if guess in previous_guesses and guess in chosen_word:
        print(f"You already chose the letter '{guess}' previously.\n")
    elif guess in previous_guesses and guess not in chosen_word:
        lifes = lifes - 1
        print(stages[lifes] + "\n")
        print(f"You already chose the letter '{guess}' previously.\nWrong Choice ! Liffe Cost : 1. \nRemaining life: {lifes}.\n")
    else:
        previous_guesses.append(guess)
        if guess not in chosen_word:
            lifes = lifes - 1
            print(stages[lifes] + "\n")
            print(f"Oops ! The chosen letter '{guess} is not fitting in there ! \nLife Cost : 1. \nRemaining life: {lifes}.\n")
        else:
            for list_index in range(0, len(chosen_word)):
                if chosen_word[list_index] == guess:
                    display.insert(list_index, guess)
                    display.pop(list_index + 1)
            
            print(stages[lifes] + "\n")
                    

    print(display)
    return lifes



game_running = True

lifes = len(stages) - 1
print(logo)
while game_running:
    if "_" not in display:
        print("\nYou won !")
        game_running = False
    elif lifes == 0:
        print("\nGame Over !")
        game_running = False
    else:
        guess = input('\nGuess a letter: ')
        guess = guess.lower()
        lifes = game_process(lifes)