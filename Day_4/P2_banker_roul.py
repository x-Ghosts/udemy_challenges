# Main objective is to create a program that will randomly select a random name from a list of names in which he or she will pay everybody's food bill
# and this, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101260#overview (Course enrolling is mandatory)



# Since I am using a VSCode environement for coding, I will use my own list of names in my side.

import random

names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

random_name = names_string[random.randint(0, len(names_string)-1)]

print(f"{random_name.title()} is going to buy the meal today !")