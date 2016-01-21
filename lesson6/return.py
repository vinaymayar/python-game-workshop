"""lesson6/return.py

Contains exercises for functions that return values.

"""

# Exercise 6: Write a function my_name that returns your name.  Remember
# to test your function by calling it and print the result.

# print(my_name()) -> "Vinay Mayar"

# Exercise 7: Write a function maximum that takes four numbers and returns
# the largest number.

# print(maximum(-3, 0, 4, 9)) -> 9

# Exercise 8: Write a function that pluralizes a word.  For most nouns,
# the plural is simply formed by adding an 's' to the end.  For nouns
# that end in 's', 'ch', 'sh', 'x', 'o', or 'z', add 'es' to the end.
# For nouns that end in 'y', replace the 'y' with 'ies'.

# HINT: You can get the last letter of a string as follows:

# string = "hello"
# string[-1] -> "o"

# and the last two letters with

# string[-2:] -> "lo"

def pluralize(word):
    last_letter = word[-1]
    last_two_letters = word[-2:]

    pluralized_word = word
    # Your code here

    return pluralized_word

print(pluralize("program")) # -> programs
print(pluralize("couch")) # -> couches
print(pluralize("kite")) # -> kites
print(pluralize("potato")) # -> potatoes
print(pluralize("flurry")) # -> flurries
