class A:
    def show(self):
        print("Show method from Class A")

class B(A):
    def show(self):
        print("Show method from Class B")

class C(A):
    def show(self):
        print("Show method from Class C")

class D(B, C):
    pass

# Create an object of D and call show()
obj = D()
obj.show()

# Show the Method Resolution Order
print(D.__mro__)
