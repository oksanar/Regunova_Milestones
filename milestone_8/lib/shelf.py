from typing import List
from lib.book import Book


class Shelf:
    __books: List[Book]
    __genries: List[str]

    def __init__(self,
                 id: int,
                 genry_type: str,
                 genries: List[str]) -> None:
        self.__id = id
        self.__genry_type = genry_type
        self.__genries = genries
        self.__books = []

    @property
    def id(self):
        return self.__id

    @property
    def genry_type(self):
        return self.__genry_type

    @property
    def genries(self):
        return self.__genries

    def add_book(self, book: Book) -> None:
        self.__books.append(book)

    def get_books(self) -> List[Book]:
        return self.__books

    def sort_books_by_title(self):
        self.__books.sort(key=lambda book: book.title)

    def to_dict(self):
        self.sort_books_by_title()
        books = []
        for book in self.__books:
            books.append(book.to_dict())
        return {
            'id': self.id,
            'genry_type': self.genry_type,
            'genries': self.genries,
            'books': books,
        }
