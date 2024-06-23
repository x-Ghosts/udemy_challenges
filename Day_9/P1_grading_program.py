# Main objective is to create a program that grades students test scores, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101340#overview (Course enrolling is mandatory)


student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

students_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        students_grades[key] = "Fail"
    elif student_scores[key]  > 70 and student_scores[key]  <= 80:
        students_grades[key] = "Acceptable"
    elif student_scores[key]  > 80 and student_scores[key]  <= 90:
        students_grades[key] = "Exceeds Expectations"
    else:
        students_grades[key] = "Outstanding"
    
print(students_grades)