from src.models.Person import Person


class Customer(Person):
    def __init__(self, lastname, firstname, year_of_birth, address, zip_code, city, country, language):
        super().__init__(lastname, firstname, year_of_birth, city, country)
        self.address = address
        self.zip_code = zip_code
        self.language = language

    def customer_introduction(self):
        print(f"{super().introduction()} Born in {self.year_of_birth}. "
              f"Located at {self.address}, {self.zip_code} in {self.city}, {self.country}. "
              f"{self.language} is the mother-language of this customer.")

    def display_customer_by_country(self, lastname, firstname, city, country):
        print(f" {firstname} {lastname}, based in {city}, {country}.")

