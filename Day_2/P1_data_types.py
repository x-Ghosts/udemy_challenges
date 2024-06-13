# Main objective is to practice on handling different types of data, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101120#overview (Course enrolling is mandatory)






## Task : Write a program that adds the digit in a 2 digit number, e.g. if the input is 35, the ouput should be 3 + 5 = 8 (Do no edit the first line of the code)






two_digit_num = input()

# Data Checking step :

print(type(two_digit_num))

# Conversion
first_digit = int(two_digit_num[0])
second_digit = int(two_digit_num[1])

# Mathematical application and Data Checking
sum_digit = first_digit + second_digit
print(sum_digit)
print(type(sum_digit))