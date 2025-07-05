from datetime import date, timedelta

class Shippable:
    def get_name(self):
        pass
    
    def get_weight(self):
        pass


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_expired(self):
        return False
    
    def is_expirable(self):
        return False

        