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


class Cart:
    def __init__(self):
        self.items = {}
    
    def add(self, product, qty):
        if qty <= 0 or qty > product.quantity:
            print(f"Invalid quantity for product: {product.name}")
            return
        if product in self.items:
            self.items[product] += qty
        else:
            self.items[product] = qty
    
    def is_empty(self):
        return len(self.items) == 0

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    

class ShippingService:
    @staticmethod
    def ship(shippables):
        print("** Shipment notice **")
        total_weight = 0
        for item in shippables:
            print(f"{item.get_name()}\t\t{int(item.get_weight()*1000)}g")
            total_weight += item.get_weight()
        print(f"Total package weight {total_weight:.1f}kg\n")


def checkout(customer, cart):
    if cart.is_empty:
        print("Error: cart is empty")
        return
    
    subtotal = 0
    shippig = 0
    shippables = []
    
    for product, qty in cart.items.items():
        if product.is_expirable() and product.is_expired():
            print(f"Error: Product {product.name} is expired")
            return

        if product.quantity < qty:
            print(f"Error: Product {product.name} out of stock.")
            return
        
        subtotal += product.price * qty
        if isinstance(product, Shippable):
            shipping += 10  # flat shipping per shippable product * qty
            for _ in range(qty):
                shippables.append(product)
    total = subtotal + shippig
    
    if customer.balance < total:
        print("Error: Insufficient balance.")
        return
    
    
    # ============================================
    for product, qty in cart.items.items():
        product.quantity -= qty
    customer.balance -= total
    
    if shippables:
        ShippingService.ship(shippables)
    
    
    # ==============================================
    print("** Checkout receipt **")
    for product, qty in cart.items.items():
        print(f"{qty}x {product.name}\t\t{int(product.price * qty)}")
    print("----------------------")
    print(f"Subtotal\t{int(subtotal)}")
    print(f"Shipping\t{int(shipping)}")
    print(f"Amount\t\t{int(total)}")
    print(f"Customer balance after payment: {int(customer.balance)}\n")