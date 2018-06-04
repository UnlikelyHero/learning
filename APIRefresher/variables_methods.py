a = 5
b = 10
my_variable = 56
my_10_variable = 10

# Variables cannot start with numbers or symbols.

string_variable = "hello"
single_quotes = 'strings can have single quotes'

# print(my_variable)
# print(string_variable)


## Section Break ##


def my_print_method(my_parameter):
    print(my_parameter)


# my_print_method("You Rock!")


def my_multiply_method(number_one, number_two):
    return number_one * number_two


result = my_multiply_method(5, 3)
# print(result)

my_print_method(my_multiply_method(5, 3))
