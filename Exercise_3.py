# In this exercise we are going to make a simple calculator that can perform basic arithmetic operations thorough user input by using if else statements.

print("Welcome to the Simple Calculator!")

operators = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operators == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operators == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operators == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operators == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"Invalid operator '{operators}'. Please use +, -, *, or /.")
print("Thank you for using the Simple Calculator!")
