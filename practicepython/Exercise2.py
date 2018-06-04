# Practice Python Exercise 2

answer = int(input("Enter any whole number: "))

test_even = answer % 2
test_4 = answer % 4

if (test_even == 0):
    if (test_4 == 0):
        print("Not only is your number even, it's divisable by 4!")
    else:
        print("Your number is even!")
else:
    print("Your number is odd!")
