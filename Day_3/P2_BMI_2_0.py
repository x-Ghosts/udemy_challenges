# Main objective is to add an interpretation related to our previous code of BMI_Calculator, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101208#overview (Course enrolling is mandatory)


# Rebuild again the BMI Calculator and include the interpretations too :

## Do not edit the code below : (base inputs : 1.55 meters, 72 kilo's)

height = float(input())
weight = int(input())

bmi = weight / (height ** 2)
bmi = round(bmi, 5)

if bmi < 18.5 :
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
