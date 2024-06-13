#####################################################
"""             Difficult Challenge               """
#####################################################



# Main objective is to build a program that works out whether if a given year is a leap year, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101222#overview(Course enrolling is mandatory)


#Do not edit this part of code :

year = int(input())

modulo_4 = year % 4
modulo_100 = year % 100
modulo_400 = year % 400

if modulo_4 == 0 :
    if modulo_100 != 0:
        print(f"The year {year} is a leap year.")
    else:
        if modulo_400 == 0:
          print(f"The year {year} is a leap year.")  
        else:
            print(f"The year {year} is not leap.")
else:
    print(f"The year {year} is not leap.")