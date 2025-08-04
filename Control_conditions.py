# Control conditions in Python
# Conditional statements

# If statement works like this:
x = 10
if x > 5:
    print("x is greater than 5")
# If-else statement
y = 20
if y < 15:
    print("y is less than 15")
else:
    print("y is not less than 15")


age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# Nested if statements
score = int(input("Enter your score: "))
if score >= 90:
    print("You got an A!")
    if score == 100:
        print("Perfect score!")
elif score >= 80:
    print("You got a B!")
else:
    print("You need to improve your score.")
# Ternary operator
is_even = True if x % 2 == 0 else False
print(f"x is even: {is_even}")
# Using logical operators
a = True
b = False
if a and b:
    print("Both a and b are True")
elif a or b:
    print("At least one of a or b is True")
else:
    print("Both a and b are False")
