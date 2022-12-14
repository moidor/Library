from src.books.repositories.BookRepository import BookRepository


class BookService(BookRepository):
    def search_a_book_by_name_service(self):
        self._search_a_book_by_name_repo()

    def search_inside_a_summary(self):
        self._search_inside_a_summary_repo()

    def search_a_book_by_year(self):
        self._search_a_book_by_year()
