"""lesson6/solution_simple_functions.py

Contains solutions for simple functions.

"""

# Exercise 1: Write a function that prints your name and try calling it.
# Work in this file and not in the Python shell.  Defining functions in
# a Python shell is difficult.  Remember to name your function something
# that indicates its purpose.

def print_my_name():
    print("Vinay Mayar")

print_my_name()

# Exercise 2: Write a function that uses your function from Exercise 1
# to print your name 10 times.

def print_my_name_ten_times():
    for ctr in range(10):
        print_my_name()

print_my_name_ten_times()
