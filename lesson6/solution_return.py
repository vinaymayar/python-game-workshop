"""lesson6/solution_return.py

Contains solutions for functions that return values.

"""

# Exercise 6: Write a function my_name that returns your name.  Remember
# to test your function by calling it and print the result.

# print(my_name()) -> "Vinay Mayar"

def my_name():
    return "Vinay Mayar"

print(my_name())

# Exercise 7: Write a function maximum that takes four numbers and returns
# the largest number.

# print(maximum(-3, 0, 4, 9)) -> 9

def maximum(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d

print(maximum(-3, 0, 4, 9))

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
    if last_letter == "y":
        pluralized_word = word[:-1] + "ies"
    elif last_letter == 's' or last_two_letters == 'ch' or \
            last_two_letters == 'sh' or last_letter == 'x' or \
            last_letter == 'o' or last_letter == 'z':
        pluralized_word = word + "es"
    else:
        pluralized_word = word + "s"

    return pluralized_word

print(pluralize("program")) # -> programs
print(pluralize("couch")) # -> couches
print(pluralize("kite")) # -> kites
print(pluralize("potato")) # -> potatoes
print(pluralize("flurry")) # -> flurries
