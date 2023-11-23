class Ticket:
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
       