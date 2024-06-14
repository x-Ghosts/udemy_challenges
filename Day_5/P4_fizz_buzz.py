# Main objective is to create a program that automatically prints the FizzBuzz solution, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101302#overview (Course enrolling is mandatory)




# The key here is the order of logic:


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # The issue is with the order of the conditions. Specifically, the condition to print "FizzBuzz" for numbers divisible by both 3 and 5 is 
        print("FizzBuzz")                   # placed after the conditions to print "Fizz" and "Buzz". Since the if and elif statements are checked sequentially, once the program evaluates
    elif number % 3 == 0:                   #  number % 3 == 0 and finds it true , it won't check further conditions for that iteration,thus skipping the elif number % 3 == 0 and number % 5 == 0 condition entirely.
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

