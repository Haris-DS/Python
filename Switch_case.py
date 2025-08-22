# # match-case statement in Python (similar to switch-case in other languages)

# # def day_of_week(day):
# #     if day == 1:
# #         return "Monday"
# #     elif day == 2:
# #         return "Tuesday"
# #     elif day == 3:
# #         return "Wednesday"
# #     elif day == 4:
# #         return "Thursday"
# #     elif day == 5:
# #         return "Friday"
# #     elif day == 6:
# #         return "Saturday"
# #     elif day == 7:
# #         return "Sunday"
# #     else:
# #         return "Invalid day"


# # print(day_of_week(3))  # Output: Wednesday
# # print(day_of_week(8))  # Output: Invalid day

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case 7:
#             return "Sunday"
#         case _:
#             return "Invalid day"


# print(day_of_week(3))  # Output: Wednesday
# print(day_of_week(8))  # Output: Invalid day


# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return "Invalid day"


# print(is_weekend("Saturday"))  # Output: True
# print(is_weekend("Monday"))    # Output: False
# print(is_weekend("Funday"))    # Output: Invalid day
