# Shopping Cart Program

item = input("What itme would you like to add to your cart? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like to add? "))

total = price * quantity

print(
    f"You have added {quantity} {item}(s) to your cart at a price of ${price:.2f} each.")
print(f"The total cost for {quantity} {item}(s) is: ${total:.2f}")
