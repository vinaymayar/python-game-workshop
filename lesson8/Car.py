class Car:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_miles(self):
        return self.miles

    def drive(self, miles):
        self.miles += miles
