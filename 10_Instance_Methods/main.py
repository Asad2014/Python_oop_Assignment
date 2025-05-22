# instance method wo hota hai jo object ke through call kiya jata hai


class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance variable
        self.breed = breed # instance variable

    def bark(self):  # instance method
        print(f"{self.name} is barking!")

if __name__ == "__main__":
    # create an instance(object)
    my_dog = Dog("Rocky", "Golden Retriever")
    # call the method
    my_dog.bark()