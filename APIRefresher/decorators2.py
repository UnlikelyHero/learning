import functools
# We need this because a decorator is going to use this library

decorators = "a function that gets called before another function"


# Define the Decorator
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func


# Apply the Decorator to the function
@my_decorator
def my_function():
    print("I'm the function!")


# Run the function, that has the decorator
# my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_function_too():
    print("hello")


my_function_too()
