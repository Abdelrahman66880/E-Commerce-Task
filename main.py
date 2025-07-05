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


class ExpirableProduct(Product):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date
    
    def is_expirable(self):
        return True
    
    def is_expired(self):
        return self.expiry_date < date.today
    
        

        