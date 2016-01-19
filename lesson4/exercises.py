# lesson4/exercises.py

# Control flow and conditionals
#
# This file contains exercises about Python conditionals.

# Last lesson, we encountered the boolean type.
# Python uses booleans to evaluate conditions.
# Last time, we directly assigned boolean values True and False, but booleans are
# also returned by comparison operations.

# 1. Comparison Operators

# There are multiple comparison operators, the most common ones are:
#   == for equality
#   != for inequality
#   > for greater than
#   < for less than
#   >= for greater than or equal
#   <= for less than or equal
#
# Don't mistake the == operator with the = operator that we learned when studying
# variables.
# The == operator (equal to) asks whether two values are the same as each other and
# returns a boolean (True or False)
# The = operator (assignment) puts the value on the right into the variable on
# the left, and returns nothing.

x = 2 # assignment!
print(x == 2) # comparison! prints out True
print(x == 3) # comparison! prints out False
print(x < 3)  # comparison! prints out True


# Exercise 1:
# Try different operators and expressions and see what they evaluate to.
# Experiment with the different types we learned: float, int and even
# strings!
# Remember, you also can compare two variables to each other!
# What happens when you try to compare strings?

# 2. Boolean Operators
# There are three boolean operators (or, and, not). These are used to formulate
# more complex boolean expressions.
#
# and, or: these are called binary operators, because they take in 2 boolean
# values.

# Uncomment the lines below, and see what they evalute to.
# print(True and True)
# print(True and False)
# print(True or True)
# print(True or False)


# The and operator evaluates an expression to True if both Boolean values are
# True; otherwise, it evaluates to False.
# The or operator evaluates an expression to True if either of the two Boolean
# values is True. If both are False, it evaluates to False.

# Truth tables
#
# and truth table:
# True and True   -> True
# True and False  -> False
# False and True  -> False
# False and False -> False
#
#
# or truth table:

# True or True   -> True
# True or False  -> True
# False or True  -> True
# False or False -> False

# The not operator only takes in a single boolean value. It simply inverts the
# boolean value.


# Uncomment the lines below and see what they evaluate to
# print(not True)
# print(not False)
# print(not not True)

# Exercise 2: Creating complex boolean expressions.
# Create three boolean expressions with at least 2 binary operators and 2
# comparison operators. Store each result in a variable and print it.
# For example,
# mybool1 = (2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
# name = "Maria"
# eggs = 5
# my_age = 21
# mybool2 = (name != "Maria" and not eggs == 5 and my_age < 18)

# Again, experiment with different variable types. See what works and what
# gives an error. If there is an error, can you find out why?


# 3. Conditionals
#
# The Python programs we've written so far have had one-track minds: they can
# add two numbers or print something, but they don't have the ability to pick
# one of these outcomes over the other.
# When developing games, sometimes we'd like our code to be able to make
# decisions.

# Control flow gives us this ability to choose among different paths depending
# on what else is happening in the program.

# The control flow statements we will be learning in this lesson are: if, elif,
# and else.
# Each of these flow control statements decides what to do based on whether its
# condition is True or False.

# In the code below, change the value of the variable name and see what happens
# In special, try making it equal to "Maria"
name = ""
if name == "Maria":
    print("Hi, Maria.")

# The if-statement seen above means the following.
# “If this condition is true, execute the code in the block.”
# In Python, an if statement consists of the following:
#   The if keyword
#   A condition (that is, an expression that evaluates to True or False)
#   A colon
#   Starting on the next line, an indented block of code (called the if block)

# VERY IMPORTANT: Identation in python.
# Lines of Python code can be grouped together in blocks. You can tell when a
# block begins and ends from the indentation of the lines of code. There are
# three rules for blocks.
#   Blocks begin when the indentation increases.
#   Blocks can contain other blocks.
#   Blocks end when the indentation decreases to zero or to an outer
#   block’s indentation.

# Blocks in Python are indented by 4 spaces more than its containing block.
# Usually, the TAB button will automatically input 4 spaces in IDLE.

# The piece code below shows how indentation works.
name = "Joana"
password = "abacate"
if name == "Joana":
    print("Hello Joana")
    if password == "abacate":
        print("Access granted.")
    else:
        print("Wrong password.")

# How many levels of indentations are there?
# How many blocks of code?

# An if-statement can optionally be followed by an else-statement.
# The else block will be executed when the if statement’s condition is False.
# Try changing the value of the variable password from the piece of code above
# and see what happens.

# The if and else statements allow us to make simple decisions. If we want to
# make our code more complex, we can use an elif statement.
# The elif statement is an “else if” statement that always follows an if or
# another elif statement. It provides another condition that is checked only
# if the previous conditions were False.
name = "Joao"
age = 16
if name == "Maria":
    print("Hi, Maria. You might be underage, but it doesn't matter :)")
elif age < 18:
    print("You are underage, and you're not Maria! Sorry.")

how_many_potatoes = 4
if how_many_potatoes > 20:
    print "lots of potatoes"
elif how_many_potatoes > 5:
    print "some potatoes, but not more than 20!"
elif how_many_potatoes > 10:
    print "the program will never get here " + \
            "because the previous case will be " + \
            "true if there are more than 5 potatoes."
elif how_many_potatoes > 0:
    print "a few potatoes"

# It is possible to have multiple elif statements.
# However, notice that an control flow statement must always start with an if
# statement and else statements, if they exist, should always be in the end.

# Exercise 3:
# To practice your newly acquired skills of control flows. Go to the file
# guard.py and fill in the blanks to create a program that detects whether
# someone should be allowed in a super secret club.

# Exercise 4:
# Now we will write our first game in python! Woooooooooah, we are so awesome!
# Go to the file guess_game.py and follow the instructions.
