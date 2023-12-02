# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Woof"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# if __name__ == "__main__":
#     animals = [Dog("Buddy"), Cat("Fluffy")]

#     for animal in animals:
#         print(f"{animal.name} makes the sound: {animal.sound()}")


from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator()]

    for i in range(20):
        rewards[randint(0, 1)].create_item().open()