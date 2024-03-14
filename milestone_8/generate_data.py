from typing import List
from faker import Faker
from random import choice
from faker.providers.isbn import Provider
import csv

fake = Faker()
fake.add_provider(Provider)


def generate_books_genres():
    fiction = [
        "Action and adventure",
        "Alternate history",
        "Anthology",
        "Chick lit",
        "Children's",
        "Classic",
        "Comic book",
        "Coming-of-age",
        "Crime",
        "Drama",
        "Fairytale",
        "Fantasy",
        "Graphic novel",
        "Historical fiction",
        "Horror",
        "Mystery",
        "Paranormal romance",
        "Picture book",
        "Poetry",
        "Political thriller",
        "Romance",
        "Satire",
        "Science fiction",
        "Short story",
        "Suspense",
        "Thriller",
        "Western",
        "Young adult"
                ]

    nonfiction = [
        "Art/architecture",
        "Autobiography",
        "Biography",
        "Business/economics",
        "Crafts/hobbies",
        "Cookbook",
        "Diary",
        "Dictionary",
        "Encyclopedia",
        "Guide",
        "Health/fitness",
        "History",
        "Home and garden",
        "Humor",
        "Journal",
        "Math",
        "Memoir",
        "Philosophy",
        "Prayer",
        "Religion, spirituality, and new age",
        "Textbook",
        "True crime",
        "Review",
        "Science",
        "Self help",
        "Sports and leisure",
        "Travel",
        "True crime"
    ]
    return [fiction, nonfiction]


def generate_data(books_number=500):
    result = []
    genries = generate_books_genres()
    genries_types = ["fiction", "nonfiction"]
    for book_id in range(1, books_number+1):
        genry_type_index = choice([0, 1])
        genry_type = genries_types[genry_type_index]
        genry = choice(genries[genry_type_index])
        row = {
            'id': book_id,
            'title': fake.unique.catch_phrase(),
            'author': f'{fake.unique.first_name()} {fake.unique.last_name()}',
            'genry_type': genry_type,
            'genry': genry,
            'isbn': str(fake.isbn13())
        }
        result.append(row)
    return result


def save_to_database(filename: str, li: List[dict]):
    headers = li[0].keys()
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(li)


if __name__ == '__main__':
    save_to_database('unsorted_books.csv', generate_data(500))
