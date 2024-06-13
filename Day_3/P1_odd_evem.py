# Main objective is to use modulo in order know if a given number is odd or even, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101198#overview (Course enrolling is mandatory)

# Even(Paire) -> Remainder after the division is 0
# Odd(Impaire) -> Remainder after division is different than 0


## Do no edit this code below :

number = int(input())
print(number)


## My part of the edit :

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")