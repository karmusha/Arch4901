# По разработанному коду нарисовать UML диаграмму. Сдаем в формате JPG. Онлайн ресурс редактор (https://online.visual-paradigm.com/)
# done
# ----------------------------------------------------------- PYTHON ------------------------------------------------------------------------------------
# 1) Переписать код в соответствии с Single Responsibility Principle: - done
from datetime import date
from typing import List

class Employee:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

class Accounting:
    def __init__(self, base_salary, employees: List[Employee]):
        self.employees = employees
        self.base_salary = base_salary
        
    def calculate_net_salary(self):
        tax = 0.25 * float(self.base_salary)  # рассчитать налог другим способом - done
        return self.base_salary - tax
    
# ​Подсказка: вынесите метод calculateNetSalary() в отдельный класс

# 2) Переписать код SpeedCalculation в соответствии с Open-Closed Principle: - cone
class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle):
        if vehicle.get_type().lower() == "car":
            return vehicle.get_max_speed() * 0.8
        elif vehicle.get_type().lower() == "bus":
            return vehicle.get_max_speed() * 0.6
        return 0.0

class Vehicle:
    def __init__(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(220, "car")
        self.brand = brand
    
class Bus(Vehicle):
    def __init__(self, brand):
        super().__init__(180, "bus")
        self.brand = brand

# Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle), напишите метод calculateAllowedSpeed(). Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP

# 3) Переписать код в соответствии с Interface Segregation Principle: - done
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2

class Cube(Shape):
    def init(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge

# Подсказка: круг не объемная фигура и этому классу не нужен метод volume().

# 4) Переписать код в соответствии с Liskov Substitution Principle: - done
class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
    
    def area(self):
        return self.side ** 2

# 5) Переписать код в соответствии с Dependency Inversion Principle: - done
class Car:
    def init(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class Engine:
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        pass

# Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.
