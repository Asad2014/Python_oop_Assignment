class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplication factor

    def __call__(self, x):
        return x * self.factor  # Multiply input by factor

# Create an instance with factor 5
m = Multiplier(5)

# Test if the object is callable
print(callable(m))  # Output: True

# Call the object like a function
result = m(10)
print(result)       # Output: 50
