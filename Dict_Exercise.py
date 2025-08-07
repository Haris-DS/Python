# # Concesion Stand Dictionary Exercise

# menu = {"hot_dog": 3.50,
#         "hamburger": 4.00,
#         "soda": 1.50,
#         "chips": 1.00,
#         "candy": 1.25,
#         "nachos": 2.50,
#         "pretzel": 2.00,
#         "popcorn": 2.75,
#         "ice cream": 3.00,
#         "water": 1.00,
#         "pizza": 9.99
#         }

# cart = []
# total = 0.0

# print("=" * 20 + " Menu " + "=" * 20)
# for key, value in menu.items():
#     print(f"{key.title():10}: ${value:.2f}")
# print("=" * 46)

# while True:
#     food = input("Select an item (q to quit): ")
#     if food == 'q'.lower():
#         break
#     elif food is not None:
#         cart.append(food)
# print("=" * 20 + " Your Order " + "=" * 20)

# for food in cart:
#     total = total + menu.get(food)
#     print(food, end=" ")
#     print()

# print("=" * 20 + " Your Bill " + "=" * 20)
# print()
# print(f"Total bill is: ${total:.2f}")
