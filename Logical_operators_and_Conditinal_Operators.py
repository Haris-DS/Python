# Logical operators in Python

# temperature = 30
# humidity = 70
# # Using 'and' operator
# if temperature > 25 and humidity < 80:
#     print("It's a warm day with acceptable humidity levels.")


# temp = 30
# is_raining = False

# if temp > 25 or temp > 100 or not is_raining:
#     print("It's either cool or not raining, or both.")
# else:
#     print("It's warm and raining.")


# temp = 30
# is_sunny = True
# if temp > 25 and is_sunny:
#     print("It's a warm and sunny day.")
# else:
#     print("It's either not warm or not sunny, or both.")

# Conditional operators in Python
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


num = 6

print("Even" if num % 2 == 0 else "Odd")
