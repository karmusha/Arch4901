from ctypes.wintypes import LONG
from decimal import Decimal
import datetime


class Ticket:
    identificator: LONG
    departure_zone: int
    arrival_zone: int
    route_number: int
    departure_time: datetime
    arrival_time: datetime
    buyer_id: LONG
    is_user: bool
    price: Decimal
    place: str

    def __init__(self, id, departure_zone, arrival_zone, route_number, departure_time, arrival_time, buyer_id, is_user, price, place):
        self.id = id
        self.departure_zone = departure_zone
        self.arrival_zone = arrival_zone
        self.route_number = route_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.buyer_id = buyer_id
        self.is_user = is_user
        self.price = price
        self.place = place

    def set_is_user(self):
        self.is_user = True
    
    def set_price(self, new_price: Decimal):
        self.price = new_price

    def get_byuer_id(self):
        return self.buyer_id
    
    def get_identificator(self):
        return self.identificator
    
    def get_price(self):
        return self.price
       