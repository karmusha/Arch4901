from abc import ABC, abstractmethod
from random import randint


class IGameItem (ABC):
    """Абстрактный класс"""

    @abstractmethod
    def open(self):
        pass

class ItemFabric (ABC):
    """Класс фабрики"""

    def create_item(self):
        pass
    
class Gold(IGameItem):
    """class Gold"""

    def open(self):
        print('Gold!')

class Gem(IGameItem):
    """class Gem"""
    
    def open(self):
        print('Gem!')

class GoldGenerator(ItemFabric):
    """Генератор от фабрики, который делает Gold"""

    def create_item(self):
        return Gold()
    
class GemGenerator(ItemFabric):
    """Генератор от фабрики, который делает Gem"""

    def create_item(self):
        return Gem()

if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator()]

    for i in range (10):
        rewards[randint(0, 1)].create_item().open()
