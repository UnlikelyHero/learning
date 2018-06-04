# Practice Python Exercise 1

name = input("Hello! What is your name?: ").strip().capitalize()
age = int(input("Nice to meet you {}! How old will you be this year?: ".format(name)))
year = 2018

till_100 = year + (100 - age)
print("Thanks {}! You'll be 100 years old by the year {}!".format(name, till_100))
count = int(input("How many years away is that?: "))
print("Okay {}, Lets see how close you were!".format(count))

while (count > 0):
    year = year + 1
    age = age + 1
    print("In {} you'll be {} years old".format(year, age))
    count = count - 1

if year == till_100 & age == 100:
    print("Great Job {}! You guessed right!".format(name))
else:
    print("OOh, so close {}! Better luck next time.".format(name))
