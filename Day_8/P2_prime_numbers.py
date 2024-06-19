# Main objective is to create a program that check whether a number is a prime number or not, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101336#overview (Course enrolling is mandatory)

import math
#We'll do the tracking with boolean values

def prime_checker(value):
    is_prime = True
    for number in range (2, value):
        if value % number == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("it's not a prime number.")





n = int(input())
prime_checker(n)