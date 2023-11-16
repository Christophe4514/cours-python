import re
import string
from pathlib import Path
from typing import List

from tinydb import TinyDB, where


class User:
    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", adress: str = "") -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.adress = adress

    def __repr__(self) -> str:
        return f"User{self.first_name}, {self.last_name}"

    def __str__(self) -> str:
        return f"{self.full_name}\n{self.phone_number}\n{self.adress}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self):
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _checks(self):
        self._check_phone_number
        self._check_name

    def _check_phone_number(self):
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digits) < 10 or not phone_digits.isdigit:
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide")

    def _check_name(self):
        if not (self.first_name and self.last_name):
            raise ValueError("le prénom et le nom de famille ne peuvent pas etre vides")

        special_characters = string.punctuation + string.digits

        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Nom invalide {self.full_name}.")

    def exists(self):
        return bool(self.db_instance)

    def delete(self) -> List[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()

        if self.exists():
            return -1
        else:
            return User.DB.insert(self.__dict__)


def get_all_user():
    return [User(**user) for user in User.DB.all()]


if __name__ == "main":
    from faker import Faker

    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    adress=fake.adress())

        print(user.save())
        print("-" * 10)
