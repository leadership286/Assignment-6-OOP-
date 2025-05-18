class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Creating some books
book1 = Book("Pride and Prejudice")
book2 = Book("To Kill a Mockingbird")
book3 = Book("1984")

print("Total books added:", Book.total_books)
