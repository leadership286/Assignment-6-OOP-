class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Testing the class
p = Product(1000)

print(p.price)      # Getting price...
p.price = 1500      # Setting price...
print(p.price)      # Getting price...

del p.price         # Deleting price...
