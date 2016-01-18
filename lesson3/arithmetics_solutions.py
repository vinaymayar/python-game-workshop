# Create two integer variables and print their sum. What is the type of the
# result?

a = 5
b = 7

print (a + b) # This prints an int.

# Now, create a float variable and print its sum with an integer variable. What
# is the type of the result.

f = 5.5

print (a + f) # This prints a float

# Divide your smallest integer value by your largest integer value. Is the
# result what you expected? Now, do the same with your float variable and an
# integer variable. What to you get?

print (a / b) # The result is 0, because the result is round to an int.

print (a / f) # The result is a float, because the result is a float, since one
              # of the operands is a float.

# Fill in the blanks, try adding the following two string variables and print
# the result. What do you get?
greeting = "My name is "
your_name = "Lara"

print(greeting + your_name) # The strings are concatenated.

# Try adding the following variables.
best_string = "I am "
your_age = 6

# This line doesn't work!
# print (best_string + your_age)
# You get the following error.
# TypeError: cannot concatenate 'str' and 'int' objects

# Although Python can add integers and floats, it can't add strings and integers.
# In order to do this, we need to convert the integer variable to a string using
# the str keyword

# Uncomment the line below and check that it works.
print(best_string + str(your_age))

# You can create complex string by using multiple string additions.
# Uncomment the line below and see the result.
print(best_string + str(your_age) + " years old")

# We can also use the float keyword and the int keyword to convert variables to
# floats and ints respectively.

my_int = 5
print(float(my_int))

# Now, convert pi to an int.

pi = 3.1415
print(int(pi))


