# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True


# print("Pyton Number Guessing Game")
# print("-------------------------------")
# print(f"Select the number between: {lowest_num} and {highest_num}")

# while is_running:
#     guess = input("Enter Your Guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("The Number is out of the range")
#             print(
#                 f"Please Select the number between: {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too Low! Try Again")
#         elif guess > answer:
#             print("Too High! Try Again")
#         else:
#             print(f"Congratulations! The Answer Was: {answer}")
#             print(f"Number of Guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid input. Please enter a number.")
#         print(
#             f"Please Select the number between: {lowest_num} and {highest_num}")
