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
    
    #Just as assumtion
    def is_expired(self):
        return self.expiry_date < date.today


class Cheese(Exception, Shippable):
    def __init__(self, name, price, quantity, expiry_date, weight):
        super().__init__(name, price, quantity, expiry_date)
        self.weight = weight
    
    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight
    

class Biscut(ExpirableProduct, Shippable):
    def __init__(self, name, price, quantity, expiry_date, weight):
        super().__init__(name, price, quantity, expiry_date)
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight
    
        

class TV(Product, Shippable):
    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight = weight
    
    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight


class MobileScratchCard(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        

class ProductFactory:
    @staticmethod
    def create_product(product_type, name, price, quantity, **kwargs):
        if product_type == "Cheese":
            expiry_date = kwargs.get('expiry_date', date.today() + timedelta(days=5))
            weight = kwargs.get('weight', 0.2)
            return Cheese(name, price, quantity, expiry_date, weight)
        elif product_type == "Biscuits":
            expiry_date = kwargs.get('expiry_date', date.today() + timedelta(days=10))
            weight = kwargs.get('weight', 0.7)
            return Biscut(name, price, quantity, expiry_date, weight)
        elif product_type == "TV":
            weight = kwargs.get('weight', 15.0)
            return TV(name, price, quantity, weight)
        elif product_type == "MobileScratchCard":
            return MobileScratchCard(name, price, quantity)
        else:
            raise ValueError(f"Unknown product type: {product_type}")

