import sqlite3
import json
from pathlib import Path

# books = json.loads(Path("books.json").read_text())
books = json.load(open("C:/Users/Cham/PycharmProjects/Library/books.json", "rb"))
# print(books)
# for book in books:
#     print(book.get("title"))


with sqlite3.connect("src/database/database.sqlite3") as conn:
    # Rechercher par langue de littérature
    # Requête : afficher la fiche de l'auteur
    # Requête : afficher livre(s) d'un auteur avec l'année de parution
    name = input("Tapez le nom de l'auteur pour afficher ses livres")
    command = f"""
    SELECT name, title, year
    FROM Books
    INNER JOIN Authors
    ON Books.id_author = Authors.id 
    WHERE Authors.name LIKE '%{name}%'  
    """
    cursor = conn.execute(command)
    books_db = cursor.fetchall()
    for book in books_db:
        if book[0] == "Fiodor Mikhaïlovitch Dostoievski":
            print(f""""{book[1]}" de Dosto est paru en {book[2]}.""")
        else:
            print(f""""{book[1]}" de {book[0]} est paru en {book[2]}.""")

    # Requête par année du livre
    # year = input("Tapez l'année du livre")
    # command = f"SELECT * FROM Books WHERE year='{year}'"
    # cursor = conn.execute(command)
    # books_db = cursor.fetchall()
    # for book in books_db:
    #     print(book[1])
    # # Requête par titre du livre
    # searched_title = input("Tapez un titre de livre")
    # command = f"SELECT * FROM Books WHERE title='{searched_title}'"
    # cursor = conn.execute(command)
    # books_db = cursor.fetchall()
    # for book in books_db:
    #     print(book[1])
    # Requête d'affichage depuis la BDD
    # command = "SELECT * FROM Books"
    # cursor = conn.execute(command)
    # # for book in books:
    # #     print(book)
    # books_db = cursor.fetchall()
    # for book in books_db:
    #     print(book[1])
#     # Insertion en BDD
#     command = "INSERT INTO Books VALUES(?, ?, ?, ?)"
#     for book in books:
#         conn.execute(command, tuple(book.values()))
#     conn.commit()
