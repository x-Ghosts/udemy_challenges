# Main objective is to create a program that calculates how many cans of paint we need to paint a wall, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101312#overview (Course enrolling is mandatory)

import numpy as np
test_h = int(input()) # Height of the wall
test_w = int(input()) # width of the wall

coverage = 5

def paint_calc(height, width, coverage):
    cans = (height * width) / coverage
    cans = np.ceil(cans)
    print(f"You'll need {int(cans)} cans of paint.")

paint_calc(test_h, test_w, coverage)