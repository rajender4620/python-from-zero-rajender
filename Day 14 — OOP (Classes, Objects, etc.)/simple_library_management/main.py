from books import Book
from library import Library

lib = Library()

b1 = Book("Python 101", "Raj")
b2 = Book("OOP Mastery", "Alex")
b3 = Book("Clean Code", "Uncle Bob")

lib.add_books(b1)
lib.add_books(b2)
lib.add_books(b3)

print("\n📚 All Books:")
lib.list_books()

# print("\n🔓 Borrowing 'Python 101':")
# lib.borrow_book("Python 101")

# print("\n📚 After Borrow:")
# lib.list_books()

# print("\n🔁 Returning 'Python 101':")
# lib.return_book("Python 101")

# print("\n📚 Final State:")
# lib.list_books()
