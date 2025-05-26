# Step 1
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Step 2: Add greet() method to the class
    return cls         

# Step 3: Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Step 4: Create an object and call greet()
p = Person("Asad")
print(p.greet())
