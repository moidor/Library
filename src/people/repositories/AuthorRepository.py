import sys
from src.database.Connection import Connection
from src.people.Author import Author
from src.interfaces.CountOfDatabase import CountOfDatabase


# conn = sqlite3.connect("C:\\Users\\Cham\\PycharmProjects\\Library\\src\\database\\database.sqlite3")


class AuthorRepository(Connection):
    def _display_books_by_author_name_repo(self):
        name = input("Display every author's books: ")
        command = f"""
            SELECT firstname, lastname, title, year
            FROM Books
            INNER JOIN Authors
            ON Books.id_author = Authors.id 
            WHERE Authors.firstname LIKE '%{name}%' OR Authors.lastname LIKE '%{name}%'  
            """
        cursor = Connection.conn.execute(command)
        authors_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(authors_db)
        for author in authors_db:
            print(f""""{author[2]}" of {author[0]} {author[1].upper()} has been published in {author[3]}.""")

    def _display_every_author_repo(self):
        input("Press \"Enter\" to display every author: ")
        command = f"""SELECT * FROM Authors"""
        cursor = Connection.conn.execute(command)
        authors_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(authors_db)
        for author in authors_db:
            # afficher l'objet "author" depuis la BDD avec la méthode de présentation
            author2 = Author(author[1], author[2], author[3], author[4], author[5], author[6])
            author2.author_introduction()

    def _display_authors_by_birthplace_repo(self):
        city = input("Display authors by their birthplace: ")
        command = f"""
                    SELECT *
                    FROM Authors
                    WHERE Authors.city LIKE '%{city}%'
                    """
        cursor = Connection.conn.execute(command)
        authors_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(authors_db)
        for author in authors_db:
            # Reformater avec l'objet "Book" comme pour l'auteur et son constructeur
            print(f"Authors born in {author[4]}, {author[5]}: \n"
                  f"- {author[2]} {author[1].upper()} in {author[3]}.")

    # Lister les auteurs par pays
    def _display_authors_by_country_repo(self):
        country = input("Display authors by their birthplace: ")
        command = f"""
                    SELECT *
                    FROM Authors
                    WHERE Authors.country LIKE '%{country}%'
                    """
        cursor = Connection.conn.execute(command)
        authors_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(authors_db)
        for author in authors_db:
            author2 = Author(author[1], author[2], author[3], author[4], author[5], author[6])
            author2.display_author_by_country(author2.lastName, author2.firstName,
                                              author2.year_of_birth, author2.city, author2.country)

    # Lister les auteurs par leur date de naissance
    def _display_authors_by_year_of_birth_repo(self):
        try:
            year_of_birth = int(input("Display authors by their year of birth: "))
        except ValueError as erreurDeValeur:
            print("Please enter an integer.", file=sys.stderr)
            print(erreurDeValeur.__doc__)
            sys.exit()
        command = f"""
                    SELECT *
                    FROM Authors
                    WHERE Authors.year_of_birth={year_of_birth}
                    """
        cursor = Connection.conn.execute(command)
        authors_db = cursor.fetchall()
        print(f"Author(s) born in {year_of_birth}:")
        CountOfDatabase.count_of_database_method(authors_db)
        for author in authors_db:
            print(f"{author[2]} {author[1].upper()} in {author[4]}, {author[5]}.")

