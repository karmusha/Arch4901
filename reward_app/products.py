from abc import ABC, abstractmethod
from typing import Any


class IGameItem (ABC):
    """Абстрактный класс"""

    @abstractmethod
    def open(self):
        pass

class Gold(IGameItem):
    """class Gold"""

    def open(self):
        print('Gold!')

class Gem(IGameItem):
    """class Gem"""

    def open(self):
        print('Gem!')

class Bronze(IGameItem):
    """class Bronze"""

    def open(self):
        print('Bronze!')

class Emerald(IGameItem):
    """class Emerald"""

    def open(self):
        print('Emerald!')

class Ruby(IGameItem):
    """class Ruby"""

    def open(self):
        print('Ruby!')

class Sapphire(IGameItem):
    """class Sapphire"""

    def open(self):
        print('Sapphire!')

class Silver(IGameItem):
    """class Silver"""

    def open(self):
        print('Silver!')
