# Main objective is to create a program that tells us how many days there are in any given month for any given year, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101576#overview (Course enrolling is mandatory)


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print("Leap Year.")
                return True
            else:
                #print("Not Leap Year.")
                return False
        else:
            #print("Leap Year.")
            return True
    else:
        #print("Not Leap Year.")
        return False

def days_in_month(year, month):
    month_days =  [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range (0, len(month_days)):
        if i+1 == month:
            if leap_year(year) == True:
                month_days.pop(i)
                month_days.insert(i, 29)
                day = month_days[i]
                return day
            else:
                day = month_days[i]
                return day



year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)