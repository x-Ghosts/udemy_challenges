# Main objective is to create a program that prints out the highest score from a list of scores, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101290#overview (Course enrolling is mandatory)


# Bloc of Code - No edit
student_scores = input().split(" ")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# The Edit side :
high_value = student_scores[0]

for n in range(0, len(student_scores) - 1):
        if student_scores[n] > student_scores[n + 1] :
            high_value = student_scores[n]
        else:
            high_value = student_scores[n+1]


print(f"The highest score in the class is: {high_value}")