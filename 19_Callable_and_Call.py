class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance
times_three = Multiplier(3)

# Check if it's callable
print(callable(times_three))  # Output: True

# Use the object like a function
print(times_three(10))        # Output: 30
print(times_three(7))         # Output: 21
