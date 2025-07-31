class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        self.__is_borrowed = False
        return True

    def is_available(self):
        return not self.__is_borrowed


book1 = Book("Python 101", "Raj")
book2 = Book("OOP Mastery", "Alex")


print(book1.is_available())  # True
book1.borrow()
print(book1.is_available())  # False
book1.return_book()
print(book1.is_available())  # True
