# Main objective is to build a Python program that uses MATHS and F-STRINGS, according to the video instructions / Task;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101144#overview (Course enrolling is mandatory)

## TASK : Create a program, using maths and f-string, that tells you how many weeks of life left, if we know that we'll live until 90 years old

age = input()

age_int = int(age)
num_weeks_per_year = 52.1429 # Ressource taken from google : https://rb.gy/7l356m (shorten URL from URL shortner)
max_year = 90 # 90 years old


remaining_years = max_year - age_int
remaining_weeks = remaining_years * num_weeks_per_year

print(f"You have {int(remaining_weeks)} weeks left.")

