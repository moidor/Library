class Person:
    def __init__(self, lastname, firstname, year_of_birth, city, country):
        self.lastName = lastname
        self.firstName = firstname
        self.year_of_birth = year_of_birth
        self.city = city
        self.country = country

    def introduction(self):
        return f"Informations: {self.firstName} {self.lastName.upper()}."
