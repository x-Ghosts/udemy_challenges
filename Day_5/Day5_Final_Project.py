# Main objective is to create a program that creates a password generator, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101308#overview (Course enrolling is mandatory)

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
new_password = '' #We'll use this to make the list of strings content join them
new_password_alternative = ''

print("Welcome to the PyPassword Generator !")
number_letters = int(input("How many letters would you like in your password ? \n"))
number_of_numbers = int(input("How many numbers would you like in your password ? \n"))
number_symbols = int(input("How many symbols would you like in your password ? \n"))

password_list = []


for input_value in range(0,number_letters):
    letter_random = letters[random.randrange(0,len(letters))]
    password_list.append(letter_random)

for input_value in range(0,number_of_numbers):
    number_random = numbers[random.randrange(0,len(numbers))]
    password_list.append(number_random)

for input_value in range(0,number_symbols):
    symbol_random = symbols[random.randrange(0,len(symbols))]
    password_list.append(symbol_random)

# Do no assign it into a variable, there is no output to expect, since the shuffle does in its place. The key to save the data is make a previous COPY
random.shuffle(password_list)
print(password_list)

new_password = new_password.join(password_list)

# Alternative :
# The character in a string is also like an index in a list
for character in password_list:
    new_password_alternative += character

print(f"Here is your password: {new_password}")

print(f"! ALTERNATIVE METHOD ! Here is your password: {new_password_alternative}")



