# Keyword Arguments = An argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


def hello(greeting, title, fname, lname):
    print(f"{greeting} {title}.{fname} {lname}")


# arguments by position
# print(hello("Hello", "Mr", "James", "John"))

# arguments by keyword
# print(hello("Hello", "Mr", lname="James", fname="John"))
