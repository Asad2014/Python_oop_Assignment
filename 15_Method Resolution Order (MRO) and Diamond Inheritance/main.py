class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):  # Multiple inheritance
    pass

# Create object of class D
d = D()
d.show()

# Display Method Resolution Order
print(D.__mro__)
