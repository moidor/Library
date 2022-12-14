from src.database.Connection import Connection


def customers_stream(customer_lastname, customer_firstname, year_of_birth, address, zip_code, city, country, language):
    # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
    if "'" in customer_lastname or customer_firstname or address or city or country or language:
        new_customer_lastname = customer_lastname.replace("'", "\'")
        new_customer_firstname = customer_firstname.replace("'", "\'")
        new_address = address.replace("'", "\'")
        new_country = country.replace("'", "\'")
        new_city = city.replace("'", "\'")
        print(f"Customer: {new_customer_firstname} {new_customer_lastname}, born in {year_of_birth}"
              f" - resident at {new_address} {zip_code} {new_city}, {new_country} - Reading language: {language}")

        # Insertion des données dans la table Customers
        command = f"""
                        INSERT INTO Customers (lastname, firstname, year_of_birth, address, 
                        zip_code, city, country, language)
                        VALUES ("{new_customer_lastname}", "{new_customer_firstname}", {year_of_birth}, "{new_address}",
                        {zip_code}, "{new_city}", "{new_country}", "{language}");
                    """
        duplicate_rows_removing = f"""
                            DELETE FROM Customers
                                WHERE id NOT IN (
                                Select MIN(id)
                                from Customers
                                group by lastname, firstname, address
                                );          
                            """
        Connection.conn.execute(command)
        Connection.conn.execute(duplicate_rows_removing)
        Connection.conn.commit()
        print(Connection.conn.cursor().rowcount, "Customer inserted in the Authors table.")


class Customers_stream:
    pass
