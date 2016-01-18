# Exercise 4: Bill calculator.

# The total cost of your meal was 44.85 reais. However, there's a tax of 6.75%
# added to that. Moreover, there's still a 10% service charge.

# Use your newly acquired coding skills to create a calculator for your meal.


your_name = "Lara"

meal_price = 44.85
tax = meal_price * 6.75 / 100 # you can you the "/" operator
service = meal_price * 0.1    # or just write the decimal number itself.
meal_final_price = meal_price + tax + service

print (your_name + "'s calculator says the total price is: " + str(meal_final_price) + " reais")

# Try writing the tax value using the "/" operator.


# Bonus: How could you write your bill calculator using less variables?
# What are the advantages and the disadvantages of that?
# You can remove meal_final_price and instead just reassign meal_price.
# This avoids using unnecessary variables, but also prevents you from retrieving
# the original meal_price if you need it in the future.
meal_price = 44.85
tax = meal_price * 6.75 / 100
service = meal_price * 0.1
meal_price = meal_price + tax + service

print (your_name + "'s calculator says the total price is: " + str(meal_price) + " reais")


# Bonus 2: How could you write the calculator in 1 line of code (not counting
# the print statement).
meal_price = 44.85 + 44.85 * 6.75/100 + 44.85 * 0.1

print (your_name + "'s calculator says the total price is: " + str(meal_price) + " reais")


# However, this is not very good practice, since now, it you wanted to change
# the initial value of the meal, you would need to change all three times
# "44.85" appears. Ideally, values that appear frequently should be stored on
# varibles.

# Bonus 3: Instead of always having the same vaue for the meal. Ask the user how
# much was their meal. You can do this by replacing "44.85" for "input()"
# Something like:
# meal_price = input()
# The above line will make your program wait for the user to type something and
# press 'enter'
# Don't forget to add a print statement before asking for use input!

print("How much did your meal cost?") # print statement asking for user input
meal_price = input() # stores user input in a variable
tax = meal_price * 6.75 / 100
service = meal_price * 0.1
meal_final_price = meal_price + tax + service

print (your_name + "'s calculator says the total price is: " + str(meal_final_price) + " reais")
