"""lesson6/challenge.py

Contains challenge exercises for functions.

"""

# Exercise: Calculator.  Write a function calculator that takes three
# inputs, a number, an operator (as a string), and another number.  The
# function should apply the specified operator to the two numbers and
# print the result.

# print(calculator(5, "+", 8)) -> 13
# print(calculator(5, "*", 8)) -> 40
# print(calculator(5, "/", 8)) -> 0 in Python 2.7; 0.625 in Python 3.x
# print(calculator(5, "-", 8)) -> -3
# print(calculator(5, "**", 2)) -> 25
# print(calculator(93, "%", 5)) -> 3

def calculator(first_number, operator, second_number):
    # Your code here
    pass

# Exercise: Alias a function.  You can create an alias for a function
# by assigning a new variable to that function:

# calc = calculator
# calc(5, "+", 8) -> 13

# Go back over a previous exercise and create an alias for one of your
# functions.  Then, use this alias to call the function.

######################################################################

# Recursion

# Python functions can call other functions as subroutines.  They can also
# call themselves as a subroutine.  This is called recursion.

# To avoid an infinite loop, the function must return a concrete value under
# certain conditions.  These conditions are called the "base cases."

# We can square a number n times as follows:

def square_n_times(number, n):
    # Base case:
    if n == 0:
        return number

    return square_n_times(number**2, n - 1)

# 3 squared two times is 3^2^2 = 3^4 = 81
print(square_n_times(3, 2)) # -> 81

# Exercise: Fibonacci
#
# Recall the fibonacci sequence.  The nth fibonacci number is equal to the
# sum of the (n-1)th and the (n-2)th fibonacci numbers.  The first two
# fibonacci numbers are 0 and 1.

# fib_0 = 0
# fib_1 = 1
# fib_2 = fib_0 + fib_1 = 0 + 1 = 1
# ...
# fib_8 = fib_6 + fib_7 = 8 + 13 = 21

# Use recursion to write a method fibonacci that returns the nth fibonacci
# number

# HINT: First consider the two base cases.  Then think about how to return
# the nth fibonacci number in terms of other fibonacci numbers.

def fibonacci(n):
    # Your code here
    pass

# Exercise: Collatz Conjecture
#
# The Collatz conjecture is a famous mathematical curiosity.  The conjecture
# states that, given any positive integer n, the following process will
# eventually yield the number 1:

# 1. If n is odd, divide n by 2. (n -> n/2)
# 2. If n is even, multiply n by 3 and add 1. (n -> 3*n + 1)

# This conjecture holds for every number that has been tested, but it has
# never been proved to hold true for all numbers.

# Your task is to determine the number of steps of the above process it takes
# to reach 1 starting at a number n.  We call the number of steps it takes to
# reach 1 the nth hailstone number.

# Consider the case where n is 3:

# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# This takes 7 steps, so the 3rd hailstone number is 7.

# Complete the hailstone function below, to compute the nth hailstone number
# given a positive integer n.

def hailstone(n):
    # Your code here
    pass
