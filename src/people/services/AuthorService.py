# On importe ici la classe AuthorRepository comme un objet et non un module
from src.people.repositories.AuthorRepository import AuthorRepository


class AuthorService(AuthorRepository):
    def display_books_by_author_name_service(self):
        self._display_books_by_author_name_repo()

    def display_every_author_service(self):
        self._display_every_author_repo()

    def display_authors_by_birthplace_service(self):
        self._display_authors_by_birthplace_repo()

    def display_authors_by_country_service(self):
        self._display_authors_by_country_repo()

    def display_authors_by_year_of_birth_service(self):
        self._display_authors_by_year_of_birth_repo()
