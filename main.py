from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sai():
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def sai(self):
        print("Woof!")

if __name__ == "__main__":
    dog = Dog()
    dog.sai()