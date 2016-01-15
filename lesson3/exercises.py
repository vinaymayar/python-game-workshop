# lesson3/exercises.py

# Variables
#
# This file contains exercises about Python variables.


# Variables

# 1) What's a variable?

# Creating web apps, games, and search engines all involve storing and working with different types of data.
# They do so using variables. A variable stores a piece of data, and gives it a specific name.

# For example:

spam = 5
# The variable spam now stores the number 5. This is called an "assignment".

# Note the ordering of the code. The variable spam on the left side of the =, and the number 5 on the right.

# TODO: Add note on what are allowed variable names.

'''
Exercise 1:

Set the variable my_variable equal to the value 10.

Hint:
'''

# 2) Variable types

# Numbers are one data type we use in programming. There are many other types used in programming. In this lesson, we will learn about four of them.
# The first data type is called an int and you used it to represent the value 10 in the my_variable from exercise 1.
# As the name suggests, ints represent integer numbers like 0, 1, 2, -5, etc.

# Another data type is called a float. Floats also represent numbers, but more specifically, they represent decimal numbers, like 1.23, 3.14, -1.00, etc
# You can use variables to store floats like this:
pi = 3.1415

# A third data type is called a boolean.
# A boolean is like a light switch. It can only have two values. Just like a light switch can only be on or off, a boolean can only be True or False.

# You can use variables to store booleans like this:
a = True
b = False
# Note that both True and False have their first letter capitalized.

# At last, the final data type we will be learning in this lesson is a string.
# A string is used to represent words, phrases or characters. Strings are always defined either with a single quote or a double quotes.

my_first_string = "Hello World!"
my_second_string = 'Hello World!'

# The difference between the two is that using double quotes makes it easy to include apostrophes.
mystring = "Don't worry about apostrophes"


'''
Exercise 2
Set the following variables to the corresponding values:

my_int to the value 7
my_float to the value 1.23
my_bool to the value True
my_string to your name.

'''

# 3. Reassinging variables
# Now you know how to use variables to store values.

# Say my_int = 7. You can change the value of a variable by "reassigning" it, like this:

'''
Exercise 3
Change the value of my_int from 7 to 3.
'''

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3!
# ADD YOUR CODE HERE!

# This line will print the varible my_int to the console:

print my_int


'''
Final exercise: Bill calculator.

The total cost of your meal was 44.85 reais. However, there's a tax of 6.75% added to that. Moreover, there's still a 10% service charge.

Use your newly acquired coding skills to create a calculator for your meal.

'''

your_name = ""

print your_name + "'s calculator says the total price is: "


