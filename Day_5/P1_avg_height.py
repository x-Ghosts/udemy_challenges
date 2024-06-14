# Main objective is to create a program that calculates the average student height from an input list by the user's choice, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101278#overview (Course enrolling is mandatory)



# Base code - Do not edit
student_heights = input().split(" ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# My part is to print : AVG, SUM of heights and total of the student.


# I created variables that will be used for outputs
count_student = 0
height = 0
avg_height = 0

# I'm looping and getting the information from the list :

for student_height in student_heights:
    count_student += 1
    height += student_height

avg_height = height / count_student

print(f"total height = {height}")
print(f"number of students = {count_student}")
print(f"average height = {int(avg_height)}")
