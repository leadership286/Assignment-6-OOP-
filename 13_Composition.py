class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car
my_car = Car(my_engine)

# Start the car (which starts the engine)
print(my_car.start_car())  # Output: Engine started.
