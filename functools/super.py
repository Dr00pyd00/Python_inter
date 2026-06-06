
class Animal:
    def __init__(self, name):
        self.name = name 
        print(f"animal créé: {self.name}")


class Dog(Animal):
    def __init__(self, name, race):
        super().__init__(name)
        self.race = race
        print(f"Dog created race = {self.race}")



d = Dog(name="dodo", race="labrador")

