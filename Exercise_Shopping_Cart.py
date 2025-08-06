# foods = []
# price = []
# total = 0

# while True:
#     food = input("Enter food item (or press 'q' to quit): ")
#     if food.lower() == 'q':
#         break
#     else:
#         price_input = float(input(f"Enter price for {food}: $ "))
#         foods.append(food)
#         price.append(price_input)

# print("*" * 5 + " Your Cart " + "*" * 5)

# for food in foods:
#     index = foods.index(food)
#     print(f"{food} - ${price[index]:.2f}")

# for prices in price:
#     total += prices
# print()
# print(f"Total: ${total:.2f}")
# print("*" * 5 + " End of Cart " + "*" * 5)
# print("Thank you for shopping with us!")
