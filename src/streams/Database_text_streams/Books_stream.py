from src.database.Connection import Connection


def books_stream(book_title, book_year, summary, author_firstname, author_lastname):
    # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
    if "'" in book_title or summary or author_firstname or author_lastname:
        new_book_title = book_title.replace("'", "\'")
        new_summary = summary.replace("'", "\'")
        new_author_firstname = author_firstname.replace("'", "\'")
        new_author_lastname = author_lastname.replace("'", "\'")
        print(f"Book title: {new_book_title} "
              f"- Year: {book_year} - Summary: {new_summary[:20]}... "
              f"- Author: {new_author_firstname} {new_author_lastname}")

        # Clé étrangère : id de l'auteur. Si l'auteur est renseigné, donc ni null ni une chaîne vide
        if new_author_firstname and new_author_lastname is not None or "":
            # Alors on lance une requête SQL dans la table Authors en vue de récupérer l'id de l'auteur
            sql_author_id = f"""
                        SELECT id
                        FROM Authors
                        WHERE firstname='{new_author_firstname}' AND lastname='{new_author_lastname}';
                    """
            # Connection.conn.execute(sql_author_id)
            cursor = Connection.conn.execute(sql_author_id)
            author_id = cursor.fetchone()
            print(f"Author's id from DB: {author_id[0]} - {new_author_firstname} {new_author_lastname}")
            command = f"""
                            INSERT INTO Books (title, year, summary, author_id)
                            VALUES ("{new_book_title}", {book_year}, "{new_summary}", {author_id[0]});
                        """
            duplicate_rows_removing = f"""
                                DELETE FROM Books
                                    WHERE id NOT IN (
                                    Select MIN(id)
                                    from Books
                                    group by title
                                    );          
                                """
            Connection.conn.execute(command)
            Connection.conn.execute(duplicate_rows_removing)
            Connection.conn.commit()
            print(Connection.conn.cursor().rowcount, "Book inserted in the Books table.")
        # Si l'auteur n'est pas renseigné par son nom et prénom, alors on insère NULL dans la colonne "author_id"
        else:
            command = f"""
                            INSERT INTO Books (title, year, summary, author_id)
                            VALUES ("{new_book_title}", {book_year}, "{new_summary}", "NULL");
                        """
            duplicate_rows_removing = f"""
                                        DELETE FROM Books
                                            WHERE id NOT IN (
                                            Select MIN(id)
                                            from Books
                                            group by title
                                            );          
                                        """
            Connection.conn.execute(command)
            Connection.conn.execute(duplicate_rows_removing)
            Connection.conn.commit()
            print(Connection.conn.cursor().rowcount, "Book inserted in the Books table.")


class Books_stream:
    pass
