# This code creates a 2D list representing a numeric keypad and prints each item in a formatted way.

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for item in row:
        print(item, end=" ")
    print()
