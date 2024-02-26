from faker import Faker
import random
import csv
from datetime import datetime
from typing import List

fake = Faker()

MIN_AGE = 23
MAX_AGE = 65
departments = ["HR", "Finance", "Engineering", "R&D"]


def generate_staff(n: int):
    result = []
    current_date = datetime.now()
    for _ in range(n):
        row = {
            'name': fake.unique.name(),
            'date_of_birth': str(fake.date_of_birth(minimum_age=MIN_AGE, maximum_age=MAX_AGE)),
            'department': departments[int(random.randrange(0, len(departments)))],
            'hiring_date': str(fake.date_between_dates(date_end=current_date, date_start='-4y'))
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
    save_to_database('database.csv', generate_staff(540))