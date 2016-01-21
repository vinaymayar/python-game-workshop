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

# Exercise 1 & 2:
#   Complete the exercises in while_loop.py

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

# So far, we have been using for loops to loop through numbers
# We can use for loops to loop through characters in a String

# Example:
#   country = 'Brazil'
#   for letter in country:
#       print letter

# This example will print out the letters in Brazil

# Exercise 3 - 7:
#   Complete the exercises in for_loop.py

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

# The continue keyword can be used to skip over the remaining code in
# one iteration of a loop and go straight to the next iteration.

# We can use this to print all numbers up to 9, but skip the number 4.
for i in range(10):
    if i == 4:
        continue
    print(i)

# Exercise 8 & 9:
#   Complete the exercises in break_continue.py
