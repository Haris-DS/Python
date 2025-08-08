# import random

# options = ("rock", "paper", "scissor")

# running = True

# while running:
#     player = None
#     computer = random.choice(options)
#     while player not in options:
#         player = input("Enter a Choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print(f"Both players selected {player}. It's a tie!")
#     elif player == "rock" and computer == "scissor":
#         print(f"Rock smashes scissors! Player wins!")
#     elif player == "paper" and computer == "rock":
#         print(f"Paper covers rock! Player wins!")
#     elif player == "scissor" and computer == "paper":
#         print(f"Scissors cuts paper! Player wins!")
#     else:
#         # Changed the last line to
#         print(f"{computer} covers {player}. Computer wins!")

#     # one way
#     # play_again = input("Play Again? (y/n): ").lower()
#     # if not play_again == 'y':
#     #     running = False
#     # another way wihtout variable
#     if not input("Play Again? (y/n): ").lower() == 'y':
#         running = False
# print("Thanks for Pplaying")
