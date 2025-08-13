# *args    = allows you to pass multiple non-keyword-arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="123", city="Lahore", state="Punjab", zip="54000")


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=" ")


# shipping_label("Dr.", "Noshaad", "Malik", "Chisti", street="123",
#                city="Lahore", state="Punjab", zip="54000")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Noshaad", "Malik", "Chisti", street="123",
               city="Lahore", state="Punjab", pobox="pobox #100", zip="54000")
