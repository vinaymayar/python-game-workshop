# We learned about ints, floats, strings, lists, and dictionaries in
# previous lessons.
# Each of the above is an instance of an object.

# In object-oriented programming (OOP), everything is an object
# This is a way of thinking about computation and organizing information
# We can organize objects that share similar attributes
# For example, all Cars have four wheels
# This is different than a Bicycle, which has two wheels

# We can define new objects in Python by creating a new class
# Classes have attributes, including data and behavior/operations/methods
# Examples of data attributes include: name, color, age
#
# When creating an instance of an object, we will likely want to provide initial
# values for the attributes.
# We define an __init__ method to do this
#
# Example:
#   class Car():
#       def __init__(self, make, model, kilometers_driven):
#           self.make = make
#           self.model = model
#           self.kilometers_driven = kilometers_driven
#
# When calling a method of an object, Python always passes the object as the
# first argument.
# We use self as the name of the first argument of methods by convention.
# The "." operator is used to access an attribute of an object
#
# The above __init__ method is defining three attributes for the
# Car object: make, model, and mileage

###############################################################################

# We can create a new instance of a Car:
#   my_car = Car('Toyota', 'Camry', 3)
#
# An instance is a particular Car.
#
# Let's say I create another Car:
#   second_car = Car('Toyota', 'Corolla', 5)
#
# This is another instance of a car, so my_car and second_car are different cars.

###############################################################################

# We can add methods, so that users can interact with the object
# It is conventional to use getters and setters to retrieve and set data attributes
# outside of the class.
# The below example shows appropriate getters and setters for the Car class.
#
# Example:
#   class Car():
#       def __init__(self, make, model, kilometers_driven):
#           self.make = make
#           self.model = model
#           self.kilometers_driven = kilometers_driven
#
#       def get_make(self):
#           return self.make
#
#       def get_model(self):
#           return self.model
#
#       def get_kilometers(self):
#           return self.kilometers_driven
#
#       def set_kilometers(self, kilometers):
#           self.kilometers_driven = kilometers

###############################################################################

# Apart from getters and setters, we can add other methods
#
# Example:
#   def drive(self, kilometers):
#       self.kilometers_driven += kilometers

# To call these methods, we use the "." notation.
# Example:
#   my_car = Car('Toyota', 'Camry', 3)
#   my_car.get_make() --> returns "Camry"
#   my_car.drive(100) --> kilometers_driven is now 103

# Exercise 1:
#   * Open Car.py
#   * Run Car.py
#   * In the Python shell, create two instances of Cars
#   * Call the drive method to add kilometers
#   * Call the get_kilometers method to see the changes to the kilometers

###############################################################################

# BONUS EXERCISES

# Exercise 2:
#   Fill in the only the __init__ method, getters, and setters for the
#   Student and Circle classes in Classes.py

# Exercise 3:
#   Make instances of Student and Circle and use "." notation to get and set
#   the data attributes.
#
#   You can run the Classes.py file and create instances in the Python shell.
#
#   Play around with the getters and setters to see how the data attributes change
#
#   Example:
#       c = Circle(0, 0, 5, 'purple')
#       print(c.get_color()) --> 'purple'
#       c.set_color('pink')
#       print(c.get_color()) --> 'pink'

# Exercise 4:
#   We will create a new class, Animal
#   Open Animal.py to start!

# Exercise 5:
#   We will create a new class, SoccerPlayer
#   Open SoccerPlayer.py to start!
