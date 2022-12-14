from src.models.Person import Person


class Author(Person):

    def __init__(self, lastname, firstname, year_of_birth, city, country, language):
        super().__init__(lastname, firstname, year_of_birth, city, country)
        self.language = language

    def author_introduction(self):
        print(f"{super().introduction()} Born in {self.year_of_birth} in {self.city}, {self.country}. The books of "
              f"this author are originally written in {self.language}.")

    def display_author_by_country(self, lastname, firstname, year_of_birth, city, country):
        print(f" {firstname} {lastname}, born in {year_of_birth} in {city}, {country}.")
