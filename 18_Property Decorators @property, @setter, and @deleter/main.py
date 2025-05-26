
class Product:
    def __init__(self, price):
        self._price = price  # Yeh private variable hai (_ underscore laga hota hai)

    # Step 1: Price ko read (get) karne ke liye
    @property
    def price(self):
        print("Getting the price...")
        return self._price

    # Step 2: Price ko update (set) karne ke liye
    @price.setter
    def price(self, value):
        print("Setting the price...")
        if value < 0:
            print("Price negative nahi ho sakti")
        else:
            self._price = value

    # Step 3: Price ko delete karne ke liye
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price


# Object banaya
p = Product(100)

# Price ko read kiya
print(p.price)   # Output: 100

# Price ko update kiya
p.price = 150    # New price set

# Dobara read kiya
print(p.price)   # Output: 150

# Price ko delete kiya
del p.price
