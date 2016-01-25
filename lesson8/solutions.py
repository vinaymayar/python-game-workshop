from Car import *

# Exercise 1
my_car = Car('Toyota', 'Prius', 0)
your_car = Car('Toyota', 'Camry', 100)

my_car.drive(100)
print(my_car.get_kilometers())  #100

your_car.drive(1000)
print(your_car.get_kilometers())    #1100

# Exercise 2
class Student():
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_school(self):
        return self.school

    def set_school(self, school):
        self.school = school

class Circle():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_radius(self):
        return self.radius
    
    def get_color(self):
        return self.color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def set_radius(self, radius):
        self.radius = radius
    
    def set_color(self, color):
        self.color = color

# Exercise 3
circle = Circle(0, 0, 5, 'purple')
print(circle.get_color())
circle.set_color('pink')
print(circle.get_color())

john = Student('John', 18, 'Garfield High School')
print(john.get_school())
john.set_school('MIT')
print(john.get_school())

# Exercise 4
class SoccerPlayer:
    def __init__(self, name, position, goals_scored):
        self.name = name
        self.position = position
        self.goals_scored = goals_scored

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_goals_scored(self):
        return self.goals_scored

    def score_goal(self):
        self.goals_scored += 1

    def score_hat_trick(self):
        self.goals_scored += 3


pele = SoccerPlayer('Pele', 'Forward', 1281)
pele.score_goal()
pele.score_hat_trick()
print(pele.get_goals_scored())

# Exercise 5
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def speak(self):
        print("Oi!")

    def have_birthday(self):
        self.age += 1

pet = Animal('Dog', 11)
pet.speak()
pet.have_birthday()
print(pet.get_age())
