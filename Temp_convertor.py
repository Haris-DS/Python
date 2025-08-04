# Temperature Converter
# This script converts temperatures between Celsius, Fahrenheit, and Kelvin.

unit = input(
    "Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ")
if unit == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
elif unit == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{fahrenheit}°F is {celsius:.2f}°C and {kelvin:.2f}K")
elif unit == 'K':
    kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{kelvin}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
else:
    print("Invalid unit. Please enter C, F, or K.")
