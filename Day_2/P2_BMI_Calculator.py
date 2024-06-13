# Main objective is to build a Body Mass Indicator calculator by using Python, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101120#overview (Course enrolling is mandatory)

# Original input (This part is not allowed to be changed)
height = input() #1.75 as an input
weight = input() #80 kg


# Floats Conversion
new_height = float(height)
new_weight = float(weight)

# BMI formula and output conversion for better reading (We can try round function for easier reading)
BMI = new_weight / (new_height ** 2)
print(int(BMI))

