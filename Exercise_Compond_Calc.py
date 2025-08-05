# # Compound Calculator

# principal = 0
# rate = 0
# time = 0

# # while principal <= 0:
# #     principal = float(input("Enter the principal amount (greater than 0): "))
# #     if principal <= 0:
# #         print("Principal must be greater than 0. Please try again.")


# # while rate <= 0:
# #     rate = float(input("Enter the Interest Rate amount (greater than 0): "))
# #     if rate <= 0:
# #         print("Interest Rate must be greater than 0. Please try again.")

# # while time <= 0:
# #     time = int(input("Enter the Time (in Years): "))
# #     if rate <= 0:
# #         print("Time must be greater than 0. Please try again.")


# # If user Want to enter 0

# while True:
#     principal = float(input("Enter the principal amount (greater than 0): "))
#     if principal < 0:
#         print("Principal must be greater than 0. Please try again.")
#     else:
#         break

# while True:
#     rate = float(input("Enter the Interest Rate amount (greater than 0): "))
#     if rate < 0:
#         print("Interest Rate must be greater than 0. Please try again.")
#     else:
#         break

# while True:
#     time = int(input("Enter the Time (in Years): "))
#     if rate < 0:
#         print("Time must be greater than 0. Please try again.")
#     else:
#         break


# total = principal * (1 + rate / 100) ** time
# print(f"Total amount after {time} years is: ${total:.2f}")
# print(f"Interest earned is: ${total - principal:.2f}")
