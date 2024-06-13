# Main objective is to create a virtual coin toss program in which it will randomly tell the user "Heads" or "Tails", according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101246#overview (Course enrolling is mandatory)

import random


# We will try to randomize integer values between 0 and 1 in order to link to the final output, respectively "Tails" for 0, and "Heads" for 1.

random_int = random.randint(0,1)

if random_int == 0:
    print("Tails")
else:
    print("Heads")