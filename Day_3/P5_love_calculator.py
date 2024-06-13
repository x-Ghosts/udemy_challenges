#####################################################
"""             Difficult Challenge               """
#####################################################



# Main objective is to build a program that compares the compatibility between two persons, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101234#overview (Course enrolling is mandatory)


print("The love calculator is calcularing your score ...")
name1 = input() #Name 1
name2 = input() #Name 2


# concatenation of names :
full_names = name1.lower() + name2.lower()

value_t = full_names.count('t')
value_r = full_names.count('r')
value_u = full_names.count('u')
value_e = full_names.count('e')

total_true = value_e + value_r + value_t + value_u

value_l = full_names.count('l')
value_o = full_names.count('o')
value_v = full_names.count('v')
value_e = full_names.count('e')

total_love = value_l + value_o + value_v + value_e

#Conversion to string and concatentation 
concatenation_love_value = str(total_true) + str(total_love)
print(type(concatenation_love_value))

# Score printing
print(f"Your score is {concatenation_love_value}")


## Interpretation and conversions
if int(concatenation_love_value) < 10 or int(concatenation_love_value) > 90:
    print(f"Score is {concatenation_love_value}, you go together like coke and mentos.")
elif int(concatenation_love_value) > 40 and int(concatenation_love_value) < 50:
    print(f"Your score is {concatenation_love_value}, you are alright together.")
else:
    print(f"Your score is {concatenation_love_value}")