# По разработанному коду нарисовать UML диаграмму. Сдаем в формате JPG. Онлайн ресурс редактор (https://online.visual-paradigm.com/)
# done
# ----------------------------------------------------------- PYTHON ------------------------------------------------------------------------------------
# 1) Переписать код в соответствии с Single Responsibility Principle: - done
from datetime import datetime
from typing import List

class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = datetime.strptime(dob, '%d.%m.%Y').date()
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

class Accountant:
    employees = dict[int: Employee]

    def __init__(self, employees: dict[int: Employee] = None):
        self.employees = employees or {}

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise ValueError('Wrong object type. It should be Employee.')
        
    def calculate_net_salary(self, employee_id: int):
        if employee_id not in self.employees:
            raise ValueError('No employee found with this ID.')        
        tax = 0.25  # рассчитать налог другим способом - done
        return int(self.employees[employee_id].base_salary * (1 - tax))
    
if __name__ == '__main__':
    employee = Employee('Mike', '13.12.2000', 30_000)
    accountant = Accountant()
    accountant.add_employee(employee)
    print(accountant.calculate_net_salary(employee))

# ​Подсказка: вынесите метод calculateNetSalary() в отдельный класс

# 2) Переписать код SpeedCalculation в соответствии с Open-Closed Principle: - cone
class ISpeedCalculation:
    def calculate_allowed_speed(self):
        pass

class Vehicle:
    def __init__(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

class Car(Vehicle, ISpeedCalculation):
    def __init__(self, max_speed, type, brand):
        super().__init__(max_speed, type)
        self.brand = brand
    
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8
    
    def get_type(self):
        return 'car'
        
class Bus(Vehicle):
    def __init__(self, max_speed, type, brand, seats_count):
        super().__init__(max_speed, type)
        self.brand = brand
        self.seats_count = seats_count

    def calculate_allowed_speed(self):
            return self.get_max_speed() * 0.6

    def get_type(self):
        return 'bus'

# Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle), напишите метод calculateAllowedSpeed(). Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP

# 3) Переписать код в соответствии с Interface Segregation Principle: - done
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class ThreeDShape(ABC):
    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Cube(Shape, ThreeDShape):
    def init(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge

# Подсказка: круг не объемная фигура и этому классу не нужен метод volume().

# 4) Переписать код в соответствии с Liskov Substitution Principle: - done
class Shape(ABC):
    @abstractmethod
    def set_width(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, wight, height):
        self.width = wight
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.height * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_width(self, side):
        self.width = side
    
    def area(self):
        return self.side ** 2

# 5) Переписать код в соответствии с Dependency Inversion Principle: - done
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class PetrolEngine(Engine):
    def start(self):
        pass

# Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.
