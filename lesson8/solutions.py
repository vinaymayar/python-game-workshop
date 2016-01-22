class Student():
    def __init__(self, name, age, school):
        # Exercise 1
        self.name = name
        self.age = age
        self.school = school

    def get_name(self):
        # Exercise 3
        return self.name

    def get_age(self):
        # Exercise 3
        return self.age

    def get_school(self):
        # Exercise 3
        return self.school

    def set_school(self, school):
        # Exercise 3
        self.school = school


class Dog():
    def __init__(self, name, breed, isHungry):
        # Exercise 1
        self.name = name
        self.breed = breed
        self.isHungry = isHungry

    def get_name(self):
        # Exercise 3
        return self.name

    def get_breed(self):
        # Exercise 3
        return self.breed

    def get_isHungry(self):
        # Exercise 3
        return self.isHungry

    def set_isHungry(self, isHungry):
        # Exercise 3
        self.isHungry = isHungry


class Circle():
    def __init__(self, x, y, radius, color):
        # Exercise 1
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def get_x(self):
        # Exercise 3
        return self.x

    def get_y(self):
        # Exercise 3
        return self.y
    
    def get_radius(self):
        # Exercise 3
        return self.radius
    
    def get_color(self):
        # Exercise 3
        return self.color

    def set_x(self, x):
        # Exercise 3
        self.x = x

    def set_y(self, y):
        # Exercise 3
        self.y = y
    
    def set_radius(self, radius):
        # Exercise 3
        self.radius = radius
    
    def set_color(self, color):
        # Exercise 3
        self.color = color


# Exercise 5
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

# Exercise 6
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
