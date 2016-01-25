class Car:
    def __init__(self, make, model, kilometers_driven):
        self.make = make
        self.model = model
        self.kilometers_driven = kilometers_driven

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_kilometers(self):
        return self.kilometers_driven

    def set_kilometers(self, kilometers):
        self.kilometers_driven = kilometers

    def get_miles(self):
        miles = self.kilometers_driven / 1.609
        return miles

    def drive(self, kilometers):
        self.kilometers_driven += kilometers
