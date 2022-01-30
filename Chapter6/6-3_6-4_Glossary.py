# Think of 5 programming words you've learned about in the previous chapters
# Use these words as the keys in your glossary, and store their meanings as words
# Print each words and its meaning as neatly formatted input
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning intented on a second line

glossary = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five"}

for number in glossary:
    # stores the right side of the colon in a variable
    word = glossary[number]
    # prints the number (left side of the colon)
    print(f"\n{number}")
    # prints the variable where we stored the value on the right side of the colon
    print(f"\n  {word}")