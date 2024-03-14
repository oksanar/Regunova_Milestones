class Book:

    def __init__(self,
                 id: int,
                 title: str,
                 author: str,
                 genry_type: str,
                 genry: str,
                 isbn: str = None) -> None:
        self.__id = id
        self.__title = title
        self.__author = author
        self.__genry_type = genry_type
        self.__genry = genry
        self.__isbn = isbn

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genry_type(self):
        return self.__genry_type

    @property
    def genry(self):
        return self.__genry

    @property
    def isbn(self):
        return self.__isbn

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'genry_type': self.genry_type,
            'genry': self.genry,
            'isbn': self.isbn
        }
