# A calculator that I will expand as I learn.

# Currently supports addition, subtraction, mulitplication, division or exponentiation of two values.

input1 = 1
input2 = "op"
input3 = 1

def menu(): 
    print("Enter two values and the operation you would like to perform.")
    print("Operators: +, -, *, and ^")
    try:
        input1 = float(input("Number: "))
    except ValueError:  
        print("Please enter valid numerical input.") 
        return
    input2 = input("Operation: ")
    try:
        input3 = float(input("Number: "))
    except ValueError:  
        print("Please enter a valid numerical input.")
        return

print(menu())

def calculate(num1, operator, num2): 
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
    return answer1

print(calculate(input1, input2, input3))

#add functionality for calculating more than two values by plugging answer back in to calculate function
