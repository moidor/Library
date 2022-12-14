from src.database.Connection import Connection
from src.interfaces.CountOfDatabase import CountOfDatabase
from src.models.Book import Book


class BookRepository(Connection):
    # Rechercher un ouvrage par son titre
    def _search_a_book_by_name_repo(self):
        title = input("Search a book: ")
        command = f"""
                    SELECT *
                    FROM Books
                    WHERE Books.title LIKE '%{title}%'
                    """
        cursor = Connection.conn.execute(command)
        books_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(books_db)
        for book in books_db:
            book2 = Book(book[1], book[2], book[3])
            book2.introduce_book(book[1], book[2])

    # Rechercher dans le résumé
    def _search_inside_a_summary_repo(self):
        title = input("Search inside a summary: ")
        command = f"""
                    SELECT *
                    FROM Books
                    WHERE Books.summary LIKE '%{title}%'
                    """
        cursor = Connection.conn.execute(command)
        books_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(books_db)
        for book in books_db:
            book2 = Book(book[1], book[2], book[3])
            book2.summarize(book[1], book[2], book[3])

    # Rechercher un ouvrage par son année de parution
    def _search_a_book_by_year(self):
        year = input("Search a book by its year of publication: ")
        command = f"""
                    SELECT title, year, summary, first_name, last_name 
                    FROM Books
                    INNER JOIN Authors
                    ON Books.id_author = Authors.id 
                    WHERE Books.year LIKE '%{year}%'
                    """
        cursor = Connection.conn.execute(command)
        books_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(books_db)
        for book in books_db:
            book2 = Book(book[1], book[2], book[3])
            final = book2.list_books_by_year(book[0], book[1])
            print(f"{final} Written by {book[3]} {book[4]}.")
