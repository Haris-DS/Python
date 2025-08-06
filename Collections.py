# Collections = Single "Variable" can store multiple values
# List, Tuple, Set, Dictionary
# List [] = Ordered, Mutable (Changable), Allows Duplicates
# Tuple () = Ordered, Immutable(Not Changable), Allows Duplicates
# Set {}= Unordered, Mutable, No Duplicates
# Dictionary {Key:Value} = Unordered, Mutable, Key-Value Pairs


# list

# fruits = ["apple", "banana", "cherry"]
# print(help(fruits))
# print(dir(fruits))
# # Accessing elements
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# for x in fruits:
#     print(x)
# # Adding elements
# fruits.append("orange")
# print(fruits)
# # Removing elements
# fruits.remove("banana")
# print(fruits)
# # Length of list
# print(len(fruits))
# # Check if an item exists
# if "apple" in fruits:
#     print("Yes, 'apple' is in the fruits list")
# # Sorting the list
# fruits.sort()
# print(fruits)
# # Reversing the list
# fruits.reverse()
# print(fruits)
# fruits.insert(1, "kiwi")
# print(fruits)
# Copying the list
# fruits_copy = fruits.copy()
# print(fruits_copy)


# Sets
# fruits = {"apple", "banana", "cherry", "mango", "kiwi", "orange"}

# print(fruits)
# print(dir(fruits))
# fruits.add("orange")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.clear()
# print(fruits)

# Tuples

# fruits = ("apple", "banana", "cherry")
# print(fruits)
# print(dir(fruits))
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# for x in fruits:
#     print(x)
# This will raise an error because tuples are immutable
# fruits.append("orange")
# fruits.remove("banana")  # This will also raise an error
# print(fruits)
# print(len(fruits))  # Length of tuple
# if "apple" in fruits:
# print("Yes, 'apple' is in the fruits tuple")
# fruits_copy = fruits  # Tuples are immutable, so this will not create a new tuple
# print(fruits_copy)
# fruits.index("banana")  # Returns the index of the first occurrence of "banana"
# Returns the number of times "apple" appears in the tuple
# fruits.count("apple")
# fruits[1] = "kiwi"  # This will raise an error because tuples are immutable
# fruits.sort()  # This will raise an error because tuples do not have a sort method
# fruits.reverse()  # This will raise an error because tuples do not have a reverse method
# This will raise an error because tuples do not have an insert method
# fruits.insert(1, "kiwi")
# This will raise an error because tuples do not have a remove method
# fruits.remove("kiwi")
# fruits.pop()  # This will raise an error because tuples do not have a pop method
# fruits.clear()  # This will raise an error because tuples do not have a clear method
# This will raise an error because tuples do not have an add method
# fruits.add("orange")
# This will raise an error because tuples do not have a discard method
# fruits.discard("banana")
# This will raise an error because tuples do not have a union method
# fruits.union({"kiwi", "orange"})
# This will raise an error because tuples do not have an intersection method
# fruits.intersection({"kiwi", "orange"})
