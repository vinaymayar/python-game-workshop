# Exercise 5: Calculate areas.

# Now, do it all on your own. What's the area of a circle?

# Write a program that asks the radius of a circle and prints the value of its area.

# Rememeber that the formula for the circle's area is
#   area = pi * (radius)^2

radius = 7.0
pi = 3.1415
area = pi * (radius ** 2)

print("the area of the circle is " + str(area))

# Bonus: Experiment and try calculating the area of other shapes.

side = 15.5
square_area = side ** 2
print("the area of the square is " + str(square_area))

circle_volume = 4 / 3 * pi * (radius ** 3)

print("the volume of the circle is " + str(circle_volume))

# Bonus 2: Use the "input()" word to ask the user which radius the circle is.
# You can do this by typing "radius = input()"

print("what's the radius of your circle?")
radius = input()
pi = 3.1415
area = pi * (radius ** 2)

print("the area of the circle is " + str(area))
