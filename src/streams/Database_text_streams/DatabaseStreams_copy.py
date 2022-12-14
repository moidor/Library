import os
import traceback
from src.database.Connection import Connection


class DatabaseStreams(Connection):
    def read_files_update_DB(self):
        #   Chercher le JDD via un stream et vérifier son existence
        file = f"C:\\Users\\Cham\\Documents\\data_import_library.txt"
        file_exists = os.path.exists(file)
        print(f"Does the file exist ? {file_exists}")
        # Ouverture du fichier en mode lecture (reading) dans un bloc try/except car opération sensible
        new_list = list()
        try:
            with open(file, mode='r', encoding="utf-8") as infile:
                for line in infile:
                    if not line.strip() or line.startswith("//"):
                        continue  # ignorer les sauts de lignes et celles débutant par "//"
                    new_list.append(line)  # ajouter les autres lignes dans la liste vide afin d'itérer après
        except FileNotFoundError as file_error:
            print(f"Error_numero: {file_error.errno} - {file_error}")
            traceback.print_exc()

        # Afficher la nouvelle liste avec l'index partant de 1 au lieu de 0 dans la méthode native "enumerate()
        # print(list(enumerate(new_list, 1))) # Raccourci qui affiche une liste de tuples
        # for index, iterated_line in enumerate(new_list, 1):
        #     print(index, type(iterated_line), iterated_line)

        # Reconnaissance des termes pour déterminer dans quelle table insérer la ligne itérée (Books, Authors, etc.)
        for line in new_list:
            if line.startswith("book"):
                split_line = list(line.split(";"))  # Séparation des données afin de les importer
                book_title, book_year, summary, author_firstname, author_lastname = \
                    split_line[1], split_line[2], split_line[3], split_line[4], split_line[5]
                # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
                new_book_title, new_summary, new_author_firstname, new_author_lastname = None, None, None, None
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
                        Connection.conn.execute(command)
                        Connection.conn.commit()
                        print(Connection.conn.cursor().rowcount, "Book inserted in the Books table.")
                    else:
                        command = f"""
                                        INSERT INTO Books (title, year, summary, author_id)
                                        VALUES ("{new_book_title}", {book_year}, "{new_summary}", "NULL");
                            """
                        Connection.conn.execute(command)
                        Connection.conn.commit()
                        print(Connection.conn.cursor().rowcount, "Book inserted in the Books table.")
