from books import Book


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Library is empty.")
            return
        for book in self.books:
            status = "Available" if book.is_available() else "Borrowed"
            print(f"{book.title} by {book.author} — {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.borrow():
                    print(f"You borrowed '{book.title}'")
                else:
                    print(f"'{book.title}' is already borrowed.")
                return
        print(f"No book found with title '{title}'")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                print(f"'{book.title}' returned successfully.")
                return
        print(f"No book found with title '{title}'")
