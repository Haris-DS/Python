# Madlib Game
# Word game where you make a story by filling in the blanks with words of your choice.

print("Welcome to the Madlib Game!")
print("Please provide the following words:")
noun = input("Noun: ")
verb = input("Verb: ")
adjective = input("Adjective: ")
adverb = input("Adverb: ")
place = input("Place: ")
name = input("Name: ")
food = input("Food: ")
story = f"""Once upon a time in a {place}, there lived a {adjective} {noun}.
Every day, {name} would {verb} {adverb} while eating {food}.
One day, something unexpected happened that changed everything!"""
print("\nHere is your story:")
print(story)
print("Thanks for playing the Madlib Game!")
