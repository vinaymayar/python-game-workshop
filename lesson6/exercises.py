"""lesson6/exercises.py

This file contains exercises for functions.

"""

# A function is a block of reusable code used to serve a single purpose.
# Instead of repeating a set of instructions multiple times in your code,
# you can put the instructions in a function and use the function where
# you would have repeated the instructions.  Functions keep your code
# organized and short.

# Functions begin with the keyword 'def', followed by the name, a set
# of parentheses, and a colon.  A function's name should always describe
# its purpose.  The rules for valid function names are the same as those
# for variables.

# def do_nothing():
#     pass

# In case you haven't seen it before, 'pass' is a simple instruction in
# Python that does absolutely nothing.

# The indented block of code that follows this line comprises the contents
# of the function.  This code is executed whenever the function is called.

def print_hello():
    print("hello")

# To call a function after it has been defined using 'def', write the name
# of the function followed by a set of parentheses.

# Uncomment the following line and see what happens.
# print_hello()

# Function blocks can contain other indented blocks, such as loops and if
# statements.

def print_hello_five_times():
    for i in range(5):
        print("hello")

# Uncomment the following line and see what happens.
# print_hello_five_times()

# A function can also call other functions.

def print_hello_ten_times():
    for i in range(10):
        print_hello()

# Uncomment the following line and see what happens.
# print_hello_ten_times()

# Exercises 1-2: Do the exercises in simple_functions.py

######################################################################

# Functions with arguments

# Functions can also take arguments.  The function's behavior may
# differ depending on the argument.  An argument can be any type:
# a string, a number, a boolean, even another function.

def print_hello_n_times(n):
    for i in range(n):
        print_hello()

# Uncomment the following lines and see what happens.
# print_hello_n_times(1)
# print_hello_n_times(5)

def print_greeting(should_print_in_portuguese):
    if should_print_in_portuguese:
        print("oi")
    else:
        print("hi")

# Uncomment the following lines and see what happens.
# print_greeting(True)
# print_greeting(False)

# The argument to a function can be a variable.

# Uncomment the following lines and see what happens.
# language_is_portuguese = True
# print_greeting(language_is_portuguese)
# language_is_portuguese = False
# print_greeting(language_is_portuguese)

# Functions can take multiple arguments.  The order in which they
# appear matters.

def print_string_n_times(string, n):
    for i in range(n):
        print(string)

# Uncomment the following lines and see what happens.
# print_string_n_times("hello", 5)
# print_string_n_times(5, "hello") # This won't work.

# Exercises 3-5: Do the exercises in arguments.py

######################################################################

# The 'return' keyword

# Sometimes, a function may compute a value that we wish to use.
# Simply printing this value doesn't allow our code to use it.  To
# use a value computed by a function, we use the 'return' keyword.

def double(x):
    twice_x = x * 2
    return twice_x

# Uncomment the following line and see what happens.
# print(double(20))

# A function can return exactly once.  After a function returns a
# value, no subsequent lines in the function are executed.  If there
# is no return statement, the function returns None - a value in
# Python that represents nothing.

def double_if_greater_than_five(x):
    if x > 5:
        return double(x)

    # The following lines will not be executed if x was greater than 5.
    print("x is less than or equal to five")
    return x

# Uncomment the following lines and see what happens.
# print(double_if_greater_than_five(6))
# print(double_if_greater_than_five(4))

# Exercises 6-8: Do the exercises in return.py

######################################################################

# CHALLENGE: Do the exercises in challenge.py
