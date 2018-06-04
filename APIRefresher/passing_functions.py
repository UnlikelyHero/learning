def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


print(methodception(add_two_numbers))
# Is the same as...
print(methodception(lambda: 35 + 77))

## Section Break ##

my_list = [13, 56, 77, 484]

print(list(filter(lambda x: x != 13, my_list)))
# is the same as...
print([x for x in my_list if x != 13])
# is the same as...


def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))


## Section break ##

(lambda x: x * 3)(5)
# is the same as...


def f(x):
    return x * 3


f(5)
