class logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger destroyed")

if __name__ == "__main__":
    Log = logger()
    del Log