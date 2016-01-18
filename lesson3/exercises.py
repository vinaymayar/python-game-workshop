# lesson3/exercises.py

# Variables
#
# This file contains exercises about Python variables.


# Variables
print("What's a variable?")

# 1) What's a variable?

# Creating web apps, games, and search engines all involve storing and working with different types of data.
# They do so using variables. A variable stores a piece of data, and gives it a specific name.

# For example:

result = 10
print("5 + 5 = {}".format(result))
# The variable result now stores the number 10. This is called an "assignment".

# Note the ordering of the code. The variable result on the left side of the =, and the number 10 on the right.

# There are some restrictions on variable names.
# Variable names can't contains spaces. Instead we use underscores ("_").
# They also shouldn't contain special signs like "%"
# Try uncommenting each of the lines below and see what happens.
# Which lines work, which don't?
#  my variable = 5
#  my_variable = 10
#  9ds = 15
#  ds9 = 42
#  %correct = 100


'''
Exercise 1:

Create a variable called my_age and set its value to your current age.
At last, print the phrase "Hi! I am (your age) years old."
'''


# 2) Variable types
print("\nVariable types")
# Numbers are one data type we use in programming. There are many other types used in programming. In this lesson, we will learn about four of them.
# The first data type is called an int and you used it to represent the value 10 in the my_variable from exercise 1.
# As the name suggests, ints represent integer numbers like 0, 1, 2, -5, etc.

# Another data type is called a float. Floats also represent numbers, but more specifically, they represent decimal numbers, like 1.23, 3.14, -1.00, etc. In Python, 5 is an integer, but 5.0 is a float.
# You can use variables to store floats like this:
pi = 3.1415
print("The value of pi is {}".format(pi))

# A third data type is called a boolean.
# A boolean is like a light switch. It can only have two values. Just like a light switch can only be on or off, a boolean can only be True or False.

# You can use variables to store booleans like this:
a = True
b = False
print("a is {}, but b is {}".format(a, b))
# Note that both True and False have their first letter capitalized.

# At last, the final data type we will be learning in this lesson is a string.
# A string is used to represent words, phrases or characters. Strings are always defined either with a single quote or a double quote.

my_first_string = "Hello World!"
my_second_string = 'Hello World!'

print("This is my first string")
print(my_first_string)
print("This is my second string")
print(my_second_string)
print("They are the same. Woah!")


# The difference between the two is that using double quotes makes it easy to include apostrophes.
mystring = "Don't worry about apostrophes"


'''
Exercise 2
Create the following variables.

my_name with the value of your name
my_age with the value of your age
ice_cream_price with the value of the price of ice cream (if you don't know, guessing is totally fine)
like_rain with the value of wheter you like rain or not

'''

# print("Hi. I am {} and I am {} years old. Ice cream now costs {} reais and the fact that i like rain is {}".format(my_name, my_age, ice_cream_price, like_rain))

# Which types were the variables you created?


# 3. Reassinging variables
# Now you know how to use variables to store values.

# Say my_int = 7. This doesn't have to be the value of the variable forever.You can change the value of a variable by assigning it to a new value, or "reassigning" it.

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

print("my_int is not 7 anymore, it's {}".format(my_int))

# 4. Variables in terms of other variables.
# Not all variables need to assigned to constant values. They can also be assigned to other variables or expressions.

'''
year_i_was_born =
this_year =
my_age = this_year - year_i_was_born
'''

# We defined my_age in terms of the variables this_year and year_i_was born
# What happens to my_age if I reassign this_year or year_i_was_born?
# Reassign one of the variables and see what happens!

# You can also reassign variables in terms of itself.
x = 15 # This line assigns x to the value of 15.
x = x + 1 # This line computes the expression x+1, and assigns its value o the variable x. So, what's the final value of x?

x += 1 # This line is another way of writing x = x + 1 in Python. What's the value of x after this?


'''
Exercise 4: Bill calculator.

The total cost of your meal was 44.85 reais. However, there's a tax of 6.75% added to that. Moreover, there's still a 10% service charge.

Use your newly acquired coding skills to create a calculator for your meal.

'''


'''
your_name = ""

# print("How much did your meal cost?")
meal_price = 44.85
tax =
service =
meal_final =

print ({}"'s calculator says the total price is: {} reais".format(your_name, meal_final))
'''
# Try writing the tax value using the "/" operator.


# Bonus: How could you write your bill calculator using fewer variables?
# What are the advantages and the disadvantages of that?
# Bonus 2: How could you write the calculator in 1 line of code (not counting the print statement)?
# Bonus 3: Instead of always having the same value for the meal, ask the user how much the meal cost.
# You can do this by replacing "44.85" with "input()"
# Something like:
# meal_price = input()
# Don't forget to uncomment the print statement.

'''
Now, do it all on your own. What's the area of a circle?

Write a program that asks the radius of a circle and prints the value of its area.

Remember that the formula for the circle's area is
  area = pi * (radius)^2
'''
