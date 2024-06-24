# Main objective is to create a calculator program, according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101576#overview (Course enrolling is mandatory)




# Mathematical Operation
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2




operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

num1 = int(input("What's your first number? "))

for key in operations:
    print(key)

math_operation_input = input("Pick an operation from the line above: ")

num2 = int(input("What's your second number? "))


new_operation = operations[math_operation_input]
answer = new_operation(num1, num2)


print(f"{num1} {math_operation_input} {num2} = {answer}")

math_operation_input = input("Pick an new operation: ")
num3 = int(input("What's your third number? "))

new_operation = operations[math_operation_input]
new_answer = new_operation(answer, num3)


print(f"{answer} {math_operation_input} {num3} = {new_answer}")
