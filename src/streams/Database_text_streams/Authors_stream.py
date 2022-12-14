from src.database.Connection import Connection


def authors_stream(author_lastname, author_firstname, year_of_birth, city, country, language):
    # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
    if "'" in author_lastname or author_firstname or city or country:
        new_author_firstname = author_firstname.replace("'", "\'")
        new_author_lastname = author_lastname.replace("'", "\'")
        new_country = country.replace("'", "\'")
        new_city = city.replace("'", "\'")
        print(f"Author: {new_author_firstname} {new_author_lastname} - Year of birth: {year_of_birth}"
              f" - City: {new_city} - Country: {new_country} - Writing language: {language}")

        # Insertion des données dans la table Authors
        command = f"""
                        INSERT INTO Authors (lastname, firstname, year_of_birth, city, country, literature_language)
                        VALUES ("{new_author_lastname}", "{new_author_firstname}", {year_of_birth}, 
                        "{new_city}", "{new_country}", "{language}");
                    """
        duplicate_rows_removing = f"""
                            DELETE FROM Authors
                                WHERE id NOT IN (
                                Select MIN(id)
                                from Authors
                                group by lastname, firstname
                                );          
                            """
        Connection.conn.execute(command)
        Connection.conn.execute(duplicate_rows_removing)
        Connection.conn.commit()
        print(Connection.conn.cursor().rowcount, "Author inserted in the Authors table.")


class Authors_stream:
    pass
