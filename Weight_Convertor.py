# In this exercise, we will create a weight convertor program that allows users to input their weight and provides feedback based on the input.
print("Welcome to the Weight Convertor Program!")

weight = float(input("Please enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")
if unit == 'K':
    print(f"Your weight is {weight} kilograms.")
    pounds = weight * 2.20462
    unit = 'lbs'
    print(f"Your weight in pounds is: {pounds:.2f} lbs")
elif unit == 'L':
    print(f"Your weight is {weight} pounds.")
    kilograms = weight / 2.20462
    unit = 'kg'
    print(f"Your weight in kilograms is: {kilograms:.2f} kg")
else:
    print("Invalid input. Please enter 'K' for kilograms or 'L' for pounds.")


print("Thank you for using the Weight Convertor Program!")
