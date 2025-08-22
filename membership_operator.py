# # Membership Operators = Used to test weather a value or variable is found in a sequence (string, list, tuple, set and dictionary)
# # Two membership operators
# # in = Returns True if a sequence with the specified value is present in the object
# # not in = Returns True if a sequence with the specified value is not present in the object
# # Strings
# txt = "The best things in life are free!"
# print("free" in txt)
# print("expensive" not in txt)
# # Lists
# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)
# print("pineapple" not in fruits)
# # Tuples
# thistuple = ("apple", "banana", "cherry")
# print("cherry" in thistuple)
# print("orange" not in thistuple)
# # Sets
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)
# print("orange" not in thisset)
# # Dictionaries = We can use the membership operators to check if a key exists in a dictionary
# thisdict = {"name": "John", "age": 36}
# print("name" in thisdict)
# # The values() method returns a list of all the values in the dictionary
# print("John" not in thisdict)
# print("age" in thisdict.values())
# print(36 in thisdict.values())
# print("36" in thisdict.values())
# print(300 in thisdict.values())
# print("age" not in thisdict.values())
# print("John" not in thisdict.values())
# print(36 not in thisdict.values())
# print("36" not in thisdict.values())
# print(300 not in thisdict.values())
