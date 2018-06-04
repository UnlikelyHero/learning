vowels = 0
consonants = 0

for letter in "supercalifragilisticexpialidocious":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels and {} consonants".format(vowels, consonants))
