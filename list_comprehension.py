# List Comprehension =  A concise way to create lists in Python
#                       Compare it with traditional loops
#                       Syntax: [expression for item in iterable if condition]

# traditional loop version
# double_numbers = []
# for x in range(1, 11):
#     double_numbers.append(x * 2)

# print(double_numbers)

# list comprehension version
# double_numbers = [x * 2 for x in range(1, 11)]
# print(double_numbers)


# fruits = [fruit.upper() for fruit in ['apple', 'banana', 'cherry']]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_numbers = [num for num in numbers if num > 0]
# print(positive_numbers)  # Output: [1, 3, 5]
# negative_numbers = [num for num in numbers if num < 0]
# print(negative_numbers)  # Output: [-2, -4, -6]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)  # Output: [-2, -4, -6]


# grades = [85, 92, 78, 90, 88, 42, 95, 67, 80, 73]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)
