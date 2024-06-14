# Main objective is to create a program that calculates the sum of even numbers between 1 and the user's number input, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101302#overview (Course enrolling is mandatory)

target = int(input())

even_number = []
sum_even = 0

for number in range (0, target + 1):
    if number % 2 == 0:
        even_number.append(number)

print(even_number)

for number in even_number:
    sum_even += number

print(sum_even)