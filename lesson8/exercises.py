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
#       def __init__(self, make, model, mileage):
#           self.make = make
#           self.model = model
#           self.mileage = mileage
#
# When calling a method of an object, Python always passes the object as the
# first argument.
# We use self as the name of the first argument of methods by convention.
# The "." operator is used to access an attribute of an object
# The __init__ method is defining three attributes for the Car object: make, model, and mileage

# Exercise 1:
#   Fill in the only the __init__ method for the classes in Classes.py
#   You can ignore the methods in Classes.py that say "Exercise 3"

###############################################################################

# We can create a new instance of a Car:
#   my_car = Car('Toyota', 'Camry', 3)
#
# An instance is a particular Car
#
# Let's say I create another Car:
#   second_car = Car('Toyota', 'Corolla', 5)
#
# This is another instance of a car
# my_car and second_car are different cars

# Exercise 2:
#   * Open Car.py
#   * Create three instances of Cars

###############################################################################

# We can add methods, so that users can interact with the object
# It is conventional to use getters and setters to retrieve and set data attributes
# outside of the class.
# The below example shows appropriate getters and setters for the Car class.
#
# Example:
#   class Car():
#       def __init__(self, make, model, mileage):
#           self.make = make
#           self.model = model
#           self.mileage = mileage
#
#       def get_make(self):
#           return self.make
#
#       def get_model(self):
#           return self.model
#
#       def get_mileage(self):
#           return self.mileage
#
#       def set_mileage(self, mileage):
#           self.mileage = mileage

# Exercise 3:
#   Fill in the getters and setters for the classes in Classes.py

###############################################################################

# Apart from getters and setters, we can add other methods
#
# Example:
#       def drive(self, miles):
#           self.mileage += miles

# To call these methods, we use the "." notation.
# Example:
#   my_car = Car('Toyota', 'Camry', 3)
#   my_car.get_make() --> returns "Camry"
#   my_car.drive(100) --> mileage is now 103

# Exercise 4:
#   Make instances of Student, Dog, and Circle and use "." notation to get and set
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

##############################################################################

# We are done learning the basics of classes, so let's create our own!
# The following two exercises will go through the steps of creating a class.
# You will also need to be creative!

# Exercise 5:
#   We will create a new class, Animal
#   Open Animal.py to start!

# Exercise 6:
#   We will create a new class, SoccerPlayer
#   Open SoccerPlayer.py to start!
