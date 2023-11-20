from car_app.Car import Car
from car_app.IFuelStation import IFuelStation

class PickUp(Car, IFuelStation):
    load_capacity: int

    def __init__(self, brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity, load_capacity):
        super().__init__(brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def sweep_street():
        print('Подметаем, вжух, вжух!')

    def refill(self):
        print('Заправляемся, буль, буль!')
