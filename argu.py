# Default Arguments = A default value for certain parameters
#                     default is wsed when that argument is ommitted
#                     make your funtion more flexiable, reduces # of arguments
#                     1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)


# print(net_price(500, 0, 0.05))

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# # print(net_price(500))
# print(net_price(500, 0.1, 0))

# import time


# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")


# print(count(0, 10))

# Non-default argument follows default argument
# SyntaxError: parameter without a default follows parameter with a default
# def count(start=0, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")


# print(count(10))

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")


# print(count(10))
