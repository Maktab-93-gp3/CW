from __future__ import annotations
from hashlib import sha256


class Human:
    def __init__(self, name) -> None:
        self.name = name

    def say_hi(self):
        print(f"Hi bitch, my name is {self.name} aka your father.")


class Librarian(Human):
    def __init__(self, name, ):
        super().__init__(name)

    def add_book(self):
        pass

class Author(Human):
    def __init__(self, name):
        super().__init__(name)


class Book:
    def __init__(self, name, page_count, price, category, author) -> None:
        self.name = name
        self.page_count = page_count
        self.isbn = sha256(f'{name} {author} {category}'.encode()).hexdigest()
        self.price = price
        self.category = Category(category)
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        self._page_count = page_count

    @property
    def category(self):
        return self._category

    @property
    def author(self):
        return self._author


class Shelf:
    def __init__(self, shelf_num, category_num) -> None:
        self.shelf_num = shelf_num
        self.category_num = category_num
        self.list_of_books = []
        self._total_pages = 0

    @property
    def identification(self):
        return f"{self.shelf_num}-{self.category_num}"
    
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, totalpages):
        if self._total_pages > 10000:
            raise ValueError('shelf is full')
        self._total_pages = totalpages


    def check_capacity(self, book):
        self.total_pages += book.page_count


    def add_book(self, book: Book):
        self.check_capacity(book)
        self.list_of_books.append(book)


class Repo:
    def __init__(self):
        self.shelves = []
    
    def add_shelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def __len__(self):
        counter = 0
        for shelf in self.shelves:
            counter += len(shelf.list_of_books)
        return counter

    
class Category:
    num_of_books_in_category = {}
    
    def __init__(self, name):
        self.name = name
        self.set_num_of_books_in_category(name)
        
    @classmethod
    def set_num_of_books_in_category(cls, name):
        cls.num_of_books_in_category[name] += 1
        cls.num_of_books_in_category.setdefault(name, 0)
        
    def __len__(self):
        return self.__class__.num_of_books_in_category[self.name]
    
    def __str__(self) -> str:
        return self.name