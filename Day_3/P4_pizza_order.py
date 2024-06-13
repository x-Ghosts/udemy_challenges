# Main objective is to build an automatic pizza program that works, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101228#overview (Course enrolling is mandatory)



# Do not edit the code
print("Thanks for choosing Python Pizza Deliveries !")
size = input() #S,M,L
add_peperoni = input() # Y or N
extra_cheese = input() # Y or N
bill = 0


if size == "S":
    bill = 15
    if add_peperoni == "Y":
        bill += 2

if size == "M":
    bill = 20
    if add_peperoni == "Y":
        bill += 3

if size == "L":
    bill = 25
    if add_peperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")