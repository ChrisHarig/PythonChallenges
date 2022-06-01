# A calculator that I will expand as I learn.

# Currently supports addition, subtraction, mulitplication, division or exponentiation of two values.

print("Enter two values and the operation you would like to perform.")
print("Operators: +, -, *, and ^")

input1 = float(input("Number: ")) #catch ValueError for non numerical inputs
input2 = input("Operation: ")
input3 = float(input("Number: ")) ##catch ValueError for non numerical inputs

def calculate(num1, operator, num2): 
    if type(num1) and type(num2) == float: #should delete eventually, convenient for now.
        float(num1)
        float(num2)
        if operator == "+":
            answer1 = num1 + num2
        elif operator == "-":
            answer1 = num1 - num2
        elif operator == "*":
            answer1 = num1 * num2
        elif operator == "/":
            answer1 = num1 / num2
        elif operator == "^":
            answer1 = num1 ** num2
        else:
            answer1 = "Please enter a valid operator."
    else:
        answer1 = "Please enter valid numerical inputs."
    return answer1

print(calculate(input1, input2, input3))

#add functionality for calculating more than two values by plugging answer back in to calculate function
