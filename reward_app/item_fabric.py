from abc import ABC, abstractmethod
import random
from collections import Counter

from reward_app.products import Gem, Gold, Bronze, Emerald, Ruby, Sapphire, Silver

class ItemFabric (ABC):
    """Класс фабрики"""

    @abstractmethod
    def create_item(self):
        pass
    
class GoldGenerator(ItemFabric):
    """Генератор от фабрики, который делает Gold"""

    def create_item(self):
        return Gold()
    
class GemGenerator(ItemFabric):
    """Генератор от фабрики, который делает Gem"""

    def create_item(self):
        return Gem()

class BronzeGenerator(ItemFabric):
    """Генератор от фабрики, который делает Bronze"""

    def create_item(self):
        return Bronze()
    
class EmeraldGenerator(ItemFabric):
    """Генератор от фабрики, который делает Emerald"""

    def create_item(self):
        return Emerald()
    
class RubyGenerator(ItemFabric):
    """Генератор от фабрики, который делает Ruby"""

    def create_item(self):
        return Ruby()
    
class SapphireGenerator(ItemFabric):
    """Генератор от фабрики, который делает Sapphire"""

    def create_item(self):
        return Sapphire()
    
class SilverGenerator(ItemFabric):
    """Генератор от фабрики, который делает Silver"""

    def create_item(self):
        return Silver()

if __name__ == '__main__':
    rewards = []
    generators = 10 * [BronzeGenerator()] + \
                    10 * [EmeraldGenerator()] + \
                        10 * [RubyGenerator()] + \
                            10 * [SapphireGenerator()] + \
                                10 * [SilverGenerator()] + \
                                    3 * [GoldGenerator()] + \
                                        [GemGenerator()]

    for i in range (200):
        rewards.append(item:= random.choice(generators).create_item())

    for i in rewards:
        print(type(i).__name__)