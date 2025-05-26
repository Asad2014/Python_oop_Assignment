class Countdown:
    def __init__(self, start):
        self.current = start  # Starting number

    def __iter__(self):
        return self  # Iterator returns itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End the loop
        else:
            num = self.current
            self.current -= 1  # Move one step down
            return num

count = Countdown(5)

for number in count:
    print(number)
