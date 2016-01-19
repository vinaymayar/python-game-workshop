# Loops

# A while loop is a control flow statement that executes code repeatedly,
# while a given boolean condition is True

# While loops follow the format
# while <condition>:
#   <expression>
#   ...

# <condition> is a boolean
# If the <condition> is True, then execute all the steps inside the while loop block
# Evaluate the condition again
# If the condition is still True, execute all the steps inside while loop block again
# Repeat until the condition is False

# Example:
#
# i = 0
# while i < 5:
#   print(i)
#   i += 1

# i starts at 0
# i is less than 5, so we execute the instructions inside the while loop
#   We print 0, then increment i by 1
# Now i is 1
# We keep printing i and incrementing, until i is no longer less than 5
#
# This will print:
#   0
#   1
#   2
#   3
#   4

# Exercise 1:
#   Using a while loop, print the numbers 0 to 10

# Exercise 2:
#   Using a while loop, print all even numbers from 0 to 100

# A for loop is a control flow statement that executes code repeatedly,
# a given number of times
#
# For loops use a loop counter or variable to keep track of the iterations

# For loops follow the format
# for <variable> in <range of values>:
#   <expression>
#   ...

# <variable> starts at the lowest value in the range of possible values
# all steps inside the for loop block will be executed
# <variable> will take on the next value
# this is repeated until the range of values has been exhausted

# In Python, we can use the range function to define a range of numbers.
# range(n) outputs a list of numbers from 0 to n - 1
#   Example: range(5) --> 0, 1, 2, 3, 4

# Example:
#
# for n in range(5):
#   print(n)
#
# i starts at 0
# We print 0
# i will take on the next value, in this case, 1
# We print 1
# i will take on the next value, in this case, 2
# We print, and i takes on the next value until we are out of values

# Exercise 3:
#   Using a for loop, print the numbers 0 to 10

# Exercise 4:
#   Using a for loop, print all even numbers from 0 to 100

# Exercise 5:
#   Using for loops, print the ASCII image:
#       *
#       **
#       ***
#       ****

# Exercise 6:
#   1) Make a new variable n equal to 10
#   2) Using a for loop, calculate the sum of the numbers 0 to n

# So far, we have been using for loops to loop through numbers
# We can use for loops to loop through characters in a String

# Example:
#   country = 'Brazil'
#   for letter in country:
#       print letter

# This example will print out the letters in Brazil

# Exercise 7:
#   1) Create a new String
#   2) Print out each letter of the String

# The break keyword can be used to "break" out of a for or while loop.
# This terminates the loop and continues to the next instruction after
# the loop.

# We can now write a while loop by specifying the terminating condition
# within the indented block.  To print the numbers 0, 1, 2, 3, 4:

counter = 0
while True: # Keep going until stopped
    print("counter is {}".format(counter))
    counter += 1
    if counter == 5: # Stop when counter reaches 5
        break

# We can also print the first word in a string, and stop when we reach
# a space:

sentence = "Programming is fun!"

first_word = ""
for letter in sentence:
    if letter == " ": # Stop when we reach a space
        break
    first_word += letter

print("first word is {}".format(first_word))

# Exercise 8:
#   Use a for loop with a break to print all the characters in a
#   string until there are two consecutive characters.
#
#   For example, if the string is

sentence = "Programming is fun!"

#   The output should be "Program".  Remember that you can use
#   a variable to keep track of the previous letter, and you
#   can use == to compare two letters.

# The continue keyword can be used to skip over the remaining code in
# one iteration of a loop and go straight to the next iteration.

# We can use this to print all numbers up to 9, but skip the number 4.
for i in range(10):
    if i == 4:
        continue
    print(i)

# Exercise 9:
#   Use a loop with the continue keyword to print all numbers from
#   0 through 19, with the exception of all multiples of 5.


# BONUS EXERCISES
# We learned about the range function earlier.
# There are more ways to use the range function.
#
# Range starts at 0 by default, but we can specify a starting point.
# range(2, n) outputs a list of numbers from 2 to n - 1
#   Example: range(2, 5) --> 2, 3, 4
#
# Range increments by 1 by default
# range(2, n, 2) outputs a list of numbers from 2 to n - 1, incrementing by 2.
#   Example: range(2, 10, 2) --> 2, 4, 6, 8
#
# Documentation at https://docs.python.org/2/library/functions.html#range

# Exercise 10:
#   Using for loops, print the ASCII image:
#       ****
#       ***
#       **
#       *
#       ****
#       ***
#       **
#       *

# Exercise 11:
#   Using two for loops, print the multiplication table (tabuada) from 0 to 10

# Exercise 12:
#   1) Make a new variable n equal to 10
#   2) Using a for loop, calculate n factorial
#
#   Note: factorial is n * (n-1) * (n-2) * ... * 1

# Exercise 13:
#   1) Make a new variable n equal to 12
#   2) Using a for loop, calculate the nth Fibonacci number
#
#   Note: The Fibonacci sequence begins with 0 and 1
#         The next number is found by adding the two previous numbers
#         So, the third Fibonacci number is 0 + 1, or 1.
#         The first few are 0, 1, 1, 2, 3, 5, 8, 13.
