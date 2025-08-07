# Dictionarys for storing and managing data

# capital_cities = {
#     "USA": "Washington, D.C.",
#     "Canada": "Ottawa",
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Japan": "Tokyo",
#     "Australia": "Canberra",
#     "India": "New Delhi",
#     "Brazil": "Brasília",
#     "Russia": "Moscow",
#     "China": "Beijing",
#     "South Africa": "Pretoria",
#     "Mexico": "Mexico City",
#     "Italy": "Rome",
#     "Spain": "Madrid",
#     "United Kingdom": "London",
#     "South Korea": "Seoul",
#     "Argentina": "Buenos Aires",
#     "Egypt": "Cairo",
#     "Turkey": "Ankara",
#     "Saudi Arabia": "Riyadh",
# }

# print(dir(capital_cities))

# print(capital_cities["USA"])
# print(capital_cities["Canada"])
# print(capital_cities["France"])
# print(capital_cities.get("Germany"))

# if capital_cities.get("Germany"):
#     print("Germany is in the dictionary.")
# else:
#     print("Germany is not in the dictionary.")

# capital_cities.update({"Pakistan": "Islamabad"})
# capital_cities.pop("Turkey")
# print("Updated capital cities:", capital_cities)

# for country, capital in capital_cities.items():
#     print(f"The capital of {country} is {capital}.")
# else:
#     print("All countries and their capitals have been printed.")

# keys = capital_cities.keys()
# values = capital_cities.values()
# print("Keys:", keys)
# for key in keys:
#     print("Key:", key)
# print("Values:", values)
# for value in values:
#     print("Value:", value)

# items = capital_cities.items()
# print(items)
# for item in items:
#     print("Item:", item)

# for key, value in capital_cities.items():
#     print(f"The capital of {key} is {value}.")
