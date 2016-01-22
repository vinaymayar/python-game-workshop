"""lesson7/exercises.py

This file contains exercises for list and dictionaries.

"""
# A list is a value that contains multiple items in an ordered sequence
# A list value looks like this: ["cat", "bat", "rat", "elephant"].
# Note that each value is separated by a comma.
# You can assign list values to variables, for example:
animals = ["cat", "bat", "rat", "elephant"]

# You can also create an empty list, by doing the following
empty_list = []

###############################################################################
# Indexing into a list

# To access particular values in a list, we can index into it.
# For example, if we wanted to get the third value of the list animals, we
# would do the following
print(animals[2]) # this is going to evaluate to "rat"

# It's important to notice that index values in a list start from 0 and go to
# lenght of the list - 1, so animals[0] evaluates to "cat"

# You can also use negative indexes to index into the list in reverse order.
print(animals[-1]) # this is going to evaluate to "elephant"
print(animals[-2]) # this is going to evaluate to "rat"

# It is also possible to get slices of a list, by doing th following.
print(animals[1:3]) # This starts the slice in the second object and goes until
                    # The third object in the list -> ["bat", "rat"]

# Each entry in a list, works like a variable. That means that you can reassign
# its values by doing something like:
animals[1] = "dynossaur"
print(animals)
# Exercises:
# Do the exercises 1-2 in the indexing.py file.

###############################################################################
# Iterating through a list.

# Previously you learned to use the range() function to use for loops.
# The range function actually returns a list. For example, range(4) returns
# the list [0, 1, 2, 3].
# What the for loop actually does is iterate through each item in the list.
# For example, we can do something like this.
for i in animals:
    print(i)

# Another cool thing you can do is to test if an element is a a list by using
# the 'in' keyword
if "cat" in animals:
  print ("I have a cat!")
# You can also combine it with the not keyword and do something like

if "duck" not in animals:
  print("why don't I have a duck?")

# Exercises:
# Do exercise 3 in the iterate.py file.

###############################################################################
# List methods

# There are several important methods used in lists. The way we use
# them is by writing list.method(arguments)

# append(x) -> adds x to the end of a list
# insert(i, x) -> inserts item x in position i
# remove(x) -> removes the first item whose value is x
# pop(i) -> remove the item in position i and returns it
# index(x) -> returns the index of value x
# count(x) -> returns the number of times x appears in the list
#
# For more list methods take a look at https://docs.python.org/2/tutorial/datastructures.html
#
# For example, if we wanted to append a new animal to our animals list, we
# would do the following

animals.append("dragon") # because everyone wants a dragon

# Exercises
# Do exercises 4-5 in the list_methods.py file


###############################################################################
# Dictionaries
#
# Like a list, a dictionary is a collection of many values. But unlike indexes
# for lists, indexes for dictionaries can use many different data types, not
# just integers. Indexes for dictionaries are called keys, and a key with its
# associated value is called a key-value pair.
#
# In code, a dictionary is typed with braces, {}.

my_cat = {"size": "fat", "color": "gray", "disposition": "loud"}

# In this case, the dictionary's keys are "size", "color", and "disposition".
# The values for these keys are "fat", "gray", and "loud", respectively. You
# can access these values through their keys, by doing the following:
print("My cat is " + my_cat["size"])

print("My cat has " + my_cat["color"] + " fur.")

# Again, dictionary entries work as variable and you can reassign them by
# doing:
my_cat["size"] = "too fat"

print("My cat is " + my_cat["size"])

# You can create an empty dictionary by doing the following:
empty_dic = {}

# Exercises:
# Exercises 6: Take a look at translate.py and complete the exercise.
#
# Exercises 7: Take a look at char_freq.py and complete the exercise.

###############################################################################
# Dictionaries Methods
#  keys()   -> returns a copy of the dictionary keys in a list format
#  values() -> returns a copy of the dictionary values in a list format
#  items()  -> returns a copy of the dictionary (key, values) pairs
#
#  Since all these methods return a list, you can use them to iterate through
#  the values and keys in a dictionary in a for loop, by doing something like:
for key in my_cat.keys():
  print (key)

for value in my_cat.values():
  print (value)

for (key, value) in my_cat.items():
  print ("The key is " + key)
  print ("The value is " + value)

# Exercises:
# Do the exercises in the file dic_methods.py
##############################################################################

# More lists exercises!

# Bonus Exercises:
# Now that you know how to use list let's pratice our skills by making a
# hangman game (jogo da forca). Go to hangman.py and try completing the code.
#
# Go to the file more_list.py and do the exercises.
#
# In tictactoe.py make a tic tac toe game using a dictionary to model the game
# board.
