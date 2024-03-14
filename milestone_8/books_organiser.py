from typing import Dict, List
import csv
import json
from lib.book import Book
from lib.shelf import Shelf

books: List[Book] = []
genry_collection = dict()


def init_books_from_csv(filename: str):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            book = Book(id=item['id'],
                        title=item['title'],
                        author=item['author'],
                        genry=item['genry'],
                        genry_type=item['genry_type'],
                        isbn=item['isbn'])
            if genry_collection.get(item['genry_type']) is None:
                genry_collection[item['genry_type']] = set()
            genry_collection[item['genry_type']].add(item['genry'])
            books.append(book)


def save_to_database(filename: str, json_str: str):
    with open(filename, 'w') as json_file:
        json_file.write(json_str)


def run_organising():
    init_books_from_csv('unsorted_books.csv')
    shelfes: List[Shelf] = []
    shelfes_counter = 0
    for genry_type_key, genries in genry_collection.items():
        shelfes_counter += 1
        shelfes.append(Shelf(id=shelfes_counter,
                             genry_type=genry_type_key,
                             genries=list(genries)))

    while len(books) > 0:
        for i in range(shelfes_counter):
            shelf = shelfes[i]
            if len(books):
                book = books.pop()
                if shelf.genry_type == book.genry_type:
                    shelf.add_book(book)
    catalog: List[Dict] = []
    for shelf in shelfes:
        catalog.append(shelf.to_dict())
    save_to_database('Bob_books_room.json', json.dumps(catalog, indent=2))


if __name__ == '__main__':
    run_organising()
