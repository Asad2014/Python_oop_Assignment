class car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")


if __name__ == "__main__":
    my_car = car("Toyota")
    my_car.start()
    print(my_car.brand)