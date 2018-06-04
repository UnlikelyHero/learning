# Ask the user for a sentence

original = input(
    "Please enter a sentence: "
    ).strip().lower()

# Split the sentence into individual words

words = original.split()

# loop through the words and covert to piglatin
new_words = []

for word in words:
    # if it starts with a vowel, just add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    # Otherwise, move the first consonant cluster to end, and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        new_word = rest + cons + "ay"
        new_words.append(new_word)

# stick words back together

output = " ".join(new_words)

# output the final string

print(output)
