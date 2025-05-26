# Step 1: Define a custom exception
class InvalidAgeError(Exception):
    pass  # No special behavior needed, just inherit from Exception

# Step 2: Define the function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Step 3: Use try-except to handle the exception
try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
    print("Age is valid!")
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
