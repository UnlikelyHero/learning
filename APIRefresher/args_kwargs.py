def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 6)


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def my_list_addition(list_arg):
    return sum(list_arg)


my_long_method(3, 5, 7, 12, 14, 55)

my_list_addition([3, 5, 7, 12, 14, 55])


def additional_simplified(*args):
    return sum(args)


##
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 34, 56, name="Jose", location="UK",)
