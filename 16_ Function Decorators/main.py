# Decorator function
def log_function_call(func): # step 2
    def wrapper():  
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator
@log_function_call # step 3
def say_hello():   # step 1
    print("Hello!")

# Call the function
say_hello()  # step 4
