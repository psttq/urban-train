from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def voice():
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def voice(self):
        print("Wow")

if __name__ == "__main__":
    dog = Dog()
    dog.voice()