from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def say():
        pass

    def eat(self):
        print(f"{self.name} eating food.")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def say(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def say(self):
        print("Meow!")
        
class Pig(Animal):
    def __init__(self):
        super().__init__("Pig")

    def say(self):
        print("Hru!")
        
class Cow(Animal):
    def __init__(self):
        super().__init__("Cow")

    def say(self):
        print("Moo!")

if __name__ == "__main__":
    pig = Pig()
    pig.say()
    pig.eat()
