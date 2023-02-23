from __future__ import annotations
class Human:
    def __init__(self, name) -> None:
        self.name = name

    def say_hi(self):
        print(f"Hi bitch, my name is {self.name} aka your father.")

class Librarian(Human):
    def __init__(self, name, ):
        super().__init__(name)

class Book:
    def __init__(self, name, page_count, isbn, value, category, author) -> None:
        self.name = name
        self.page_count = page_count
        self.isbn = isbn
        self.value = value
        self.category = category
        self.author = author

class Shelf:
    def __init__(self, shelf_num, category_num) -> None:
        self.shelf_num = shelf_num
        self.category_num = category_num
        self.total_pages = 0
    @property
    def total_pages(self):
        return self.total_pages
    @total_pages.setter
    def total_pages(self, totalpages):
        if self.total_pages > 10000:
            raise ValueError ('shelf is full')

    