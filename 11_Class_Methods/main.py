#  class method wo hota hai jo class ke through call kiya jata hai

class Book:
    total_books = 0  # Class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

if __name__ == "__main__":
    Book.increment_book_count()
    
    print(f"Total books: {Book.total_books}")


