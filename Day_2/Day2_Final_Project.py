# Main objective is to build a Tip Calculator using Python, according to the video instructions / Task;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/17841394#overview (Course enrolling is mandatory)

""" Instructions :

1. Greeting Message
2. Asking the total of the bill
3. Percentage of Tip choice to give 10, 12 or 15 ?
4. Ask how much people are in there
5. Split the bill in between people"""


# The phase of testing for inputs are : 150.00 $ for the bills, number of persons are 5 and the tip percentage is 12%

print("Welcome to the tip calculator !")

bill = float(input("What was the total of the bill? $ "))
tip = int(input("How much tip you would like to give ? 10%, 12%, 15%? %"))
num_people = int(input("How many people to split the bill? "))

tip_bill = bill * (float(tip) / 100)
new_bill = float(bill) + float(tip_bill)
bill_per_people = float(new_bill) / int(num_people)
bill_per_people_rounded = round(bill_per_people, 2)

print(f"Each people should pay: ${bill_per_people_rounded}")