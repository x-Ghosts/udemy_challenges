# Main objective is to create a program that creates a password generator, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101308#overview (Course enrolling is mandatory)

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
new_password = '' #We'll use this to make the list of strings content join them

print("Welcome to the PyPassword Generator !")
number_letters = int(input("How many letters would you like in your password ? \n"))
number_of_numbers = int(input("How many numbers would you like in your password ? \n"))
number_symbols = int(input("How many symbols would you like in your password ? \n"))

new_letters = []
new_numbers = []
new_symbols = []


for input_value in range(0,number_letters):
    letter_random = letters[random.randrange(0,len(letters))]
    new_letters.append(letter_random)

for input_value in range(0,number_of_numbers):
    number_random = numbers[random.randrange(0,len(numbers))]
    new_numbers.append(number_random)

for input_value in range(0,number_symbols):
    symbol_random = symbols[random.randrange(0,len(symbols))]
    new_symbols.append(symbol_random)

print(new_letters)
print(new_numbers)
print(new_symbols)

new_password = new_password.join(new_letters)
print(new_password)
new_password = new_password.join(new_numbers)
print(new_password)
new_password = new_password.join(new_symbols)

len(new_password)
print(new_password)

