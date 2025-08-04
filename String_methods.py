# name = input("Enter your full name: ")

# # len(name)
# # print("Length of your name:", len(name))

# # result = name.find("a")
# result = name.rfind("a")
# print(result)


# Excercise: String methods in Python

# username = input("Enter your username: ")
# if len(username) > 12:
#     print("Username should not be longer than 12 characters.")
# elif not username.find(" ") == -1:
#     print("Username should not contain spaces.")
# elif not username.isalpha():
#     print("Username should only contain alphabetic characters.")

# else:
#     print(f"Welcome {username}!")


# String Indexing and Slicing in Python

# name = "John Doe"
# print("First character:", name[0])
# print("Last character:", name[-1])
# print("First three characters:", name[:3])
# print("Last three characters:", name[-3:])
# print("Middle character:", name[len(name) // 2])
# print("Characters from index 2 to 5:", name[2:6])
# print("Characters from index 2 to the end:", name[2:])
# print("Characters from the start to index 5:", name[:6])
# print("Every second character:", name[::2])
# print("Reversed string:", name[::-1])
# print("Uppercase:", name.upper())
# print("Lowercase:", name.lower())
# print("Title case:", name.title())
# print("Swap case:", name.swapcase())
# print("Count of 'o':", name.count('o'))
# print("Replace 'John' with 'Jane':", name.replace('John', 'Jane'))
# print("Split by space:", name.split())
# print("Join with hyphen:", '-'.join(name.split()))
# print("Check if starts with 'John':", name.startswith('John'))
# print("Check if ends with 'Doe':", name.endswith('Doe'))
# print("Find index of 'Doe':", name.find('Doe'))
# print("Find index of 'Doe' (not found):", name.find('Smith'))
# print("Find index of 'Doe' (not found, returns -1):", name.find('Smith', 0, 10))
# print("Check if all characters are alphabetic:", name.isalpha())
# print("Check if all characters are alphanumeric:", name.isalnum())
# print("Check if all characters are digits:", name.isdigit())
# print("Check if all characters are whitespace:", name.isspace())
# print("Check if string is numeric:", name.isnumeric())
# print("Check if string is printable:", name.isprintable())
# print("Check if string is a valid identifier:", name.isidentifier())

# credit_card = "1234-4567-8910-1234"

# # last_digits = credit_card[-4:]
# # print(f"xxxx-xxxx-xxxx-{last_digits}")

# reversed_card = credit_card[::-1]
# print(f"Reversed credit card number: {reversed_card}")
