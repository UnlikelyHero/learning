# counting
print("hello".count("e"))
text = "happy birthday"
print(text.count("a"))
print(text.count("day"))
print(len(text))       # counts the number of characters in a string

# case changing
x = "happy birthday"
print(x.lower())       # converts everything to lowercase
print(x.upper())       # converts everthing to capital
print(x.capitalize())  # converts the first letter in the string to capital
print(x.title())       # converts first letter in each word to capital

# case checking (true or false)
x = x.title()          # converts x to title case and replaces x
print(x.islower())
print(x.isupper())
print(x.istitle())
print(x.isalpha())     # contains letters, but no special characters
print(x.isdigit())     # string contains digits
print(x.isalnum())     # contains numbers and letters but no special characters

# searching in strings
x = "happy birthday"
print(x.index("birthday"))  # locates the value in the string
print(x.find("birthday"))   # locates the value in the string, but returns false if not found.
x = "0000000happybirthday0000000"
print(x.strip("0"))         # removes a value in the string.
print(x.lstrip("0"))        # removes the values from the beginning of the string.
print(x.rstrip("0"))        # removes the values from the end of the string.
x = "happy birthday    "    # extra spaces intended
print(x.strip())            # removes the spaces from the string

# slicing strings
word = "supercalifragilisticexpialidocious"
print(word[0])      # gives us "s"
print(word[2])      # gives us "p"
print(word[0:5:1])  # gives us "super" (start:end:step)
print(word[5:9:1])  # gives us "cali"
print(word[5:])     # gives us "califragilisticexpialidocious"
print(word[:8])     # gives us "supercal"
print(word[::-1])   # gives us the whole string, backwards!
print(word[-1])     # gives us the last letter in the string

print(word[word.index("cali"):word.index("expi")])
# returns "fragilistic"
