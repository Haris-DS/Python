# Dice roller program in python

import random

dice_faces = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("how Many Dice?: "))

for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for i in range(num_of_dice):
#     for j in dice_faces.get(dice[i]):
#         print(j)

for line in range(5):
    for die in dice:
        print(dice_faces.get(die)[line], end=" ")
    print()

for i in dice:
    total += i
print(f"Total: {total}")
