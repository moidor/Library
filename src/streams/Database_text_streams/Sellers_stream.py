from src.database.Connection import Connection


def sellers_stream(name, city, country):
    # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
    if "'" in name or city or country:
        new_name = name.replace("'", "\'")
        new_city = city.replace("'", "\'")
        new_country = country.replace("'", "\'")
        print(f"Seller: {new_name}, {new_city}, {new_country}")

        # Insertion des données dans la table Sellers
        command = f"""
                        INSERT INTO Sellers (name, city, country)
                        VALUES ("{new_name}", "{new_city}", "{new_country}");                                      
                    """
        duplicate_rows_removing = f"""
                    DELETE FROM Sellers
                        WHERE id NOT IN (
                        Select MIN(id)
                        from Sellers
                        group by name
                        );          
                    """
        Connection.conn.execute(command)
        Connection.conn.execute(duplicate_rows_removing)
        Connection.conn.commit()
        print(Connection.conn.cursor().rowcount, "Seller inserted in the Sellers table.")


class Customers_stream:
    pass
