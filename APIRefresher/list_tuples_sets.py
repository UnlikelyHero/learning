my_variable = "hello"

list_grades = [77, 80, 90, 95, 100]
# values can be reassigned, appended or removed

tuple_grades = (77, 80, 90, 95, 100)
# values cannot be reassigned, appended or removed

set_grades = {77, 80, 90, 100, 100}
# unique values only, and unordered

list_grades[0] = 60
list_grades.append(100)
# print(list_grades)

## Advanced Set Operations ##

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# print(set_one.intersection(set_two))
# which values match

print(set_one.union(set_two))
# combines sets, no duplications

print({1, 2, 3, 4}.difference({1, 2}))
# only displays the numbers that don't have a match

for character in my_variable:
    print(character)

for number in set_one:
    print(number ** 2)
