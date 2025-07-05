from main import *
from datetime import date, timedelta, datetime

if __name__ == "__main__":
    factory = ProductFactory()
    cheese = factory.create_product("Cheese", "Cheese", 100, 5, expiry_date=date.today()+timedelta(days=5), weight=0.2)
    biscuits = factory.create_product("Biscuits", "Biscuits", 150, 3, expiry_date=date.today()+timedelta(days=2), weight=0.7)
    tv = factory.create_product("TV", "TV", 5000, 2, weight=15.0)
    scratch_card = factory.create_product("MobileScratchCard", "ScratchCard", 50, 10)

    customer = Customer("Ali", 6000)

    cart = Cart()
    cart.add(cheese, 2)
    cart.add(biscuits, 1)
    cart.add(tv, 1)
    cart.add(scratch_card, 1)

    checkout(customer, cart)