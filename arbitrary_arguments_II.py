# *args    = allows you to pass multiple non-keyword-arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123", city="Lahore", state="Punjab", zip="54000")
