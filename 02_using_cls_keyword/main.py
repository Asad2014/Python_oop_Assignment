class counter:
    count = 0

    def __init__(self):
        counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total Objects Created: {cls.count}")
    
if __name__ == "__main__":
    c1 = counter()
    c2 = counter()
    c3 = counter()
    counter.show_count()




