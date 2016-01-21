"""lesson6/solution_arguments.py

Contains solutions for functions with arguments.

"""

# Exercise 3: Complete the function 'negate' below, which takes a number and
# prints its negative.  Remember to call your function to test that it works.

# negate(5) -> 5

def negate(x):
    print(-1 * x)

negate(5)

# Exercise 4: Write a function add that adds two numbers.

# add(4, 5) -> 9
# add(9, 3) -> 12

def add(x, y):
    print(x + y)

add(4, 5)
add(9, 3)

# Exercise 5: Complete the function below that takes a string and a character
# and prints whether the string contains the specified character.

def string_contains_character(string, character):
    found_character = False

    for letter in string:
        if letter == character:
            found_character = True
            break

    # We only reach here after going through the entire string or
    # after finding the character.
    print(found_character)

# OR

def string_contains_character_2(string, character):
    if character in string:
        print(True)
    else:
        print(False)

# OR

def string_contains_character_3(string, character):
    print(character in string)

string_contains_character("hello", "e")
string_contains_character_2("hello", "e")
string_contains_character_3("hello", "e")

string_contains_character("hello", "f")
string_contains_character_2("hello", "f")
string_contains_character_3("hello", "f")
