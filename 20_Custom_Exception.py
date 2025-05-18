# Custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above"):
        self.message = message
        super().__init__(self.message)

# Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Access granted.")

# Test it out
try:
    check_age(16)  # This will raise the exception
except InvalidAgeError as e:
    print("Exception caught:", e)

# Try with valid age
try:
    check_age(21)  # This will not raise the exception
except InvalidAgeError as e:
    print("Exception caught:", e)
