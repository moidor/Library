import sys
from src.database.Connection import Connection
from src.people.Customer import Customer
from src.interfaces.CountOfDatabase import CountOfDatabase


class CustomerRepository(Connection):
    # Rechercher un client par son nom ou son prénom
    def _search_a_customer_by_name_repo(self):
        name = input("Search a customer by firstname or lastname: ")
        command = f"""
            SELECT *
            FROM Customers
            WHERE Customers.firstname LIKE '%{name}%' OR Customers.lastname LIKE '%{name}%'
            """
        cursor = Connection.conn.execute(command)
        orders_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(orders_db)
        for customer in orders_db:
            customer2 = Customer(customer[1], customer[2], customer[3], customer[4], customer[5],
                                 customer[6], customer[7], customer[8])
            customer2.customer_introduction()

    # Lister tous les clients
    def _display_every_customer_repo(self):
        input("Press \"Enter\" to display every customer: ")
        command = f"""SELECT * FROM Customers"""
        cursor = Connection.conn.execute(command)
        customers_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(customers_db)
        for customer in customers_db:
            customer2 = Customer(customer[1], customer[2], customer[3], customer[4], customer[5],
                                 customer[6], customer[7], customer[8])
            customer2.customer_introduction()

    # Lister les clients par leur ville de résidence
    def _display_customers_by_city_repo(self):
        city = input("Display customers by their city of residence: ")
        command = f"""
                    SELECT *
                    FROM Customers
                    WHERE Customers.city LIKE '%{city}%'
                    """
        cursor = Connection.conn.execute(command)
        customers_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(customers_db)
        for customer in customers_db:
            print(f"Customer(s) based in {customer[4]}, {customer[5]}: \n"
                  f"- {customer[2]} {customer[1].upper()} in {customer[3]}.")

    # Lister les clients par pays
    def _display_customers_by_country_repo(self):
        country = input("Display customers by their country of residence: ")
        command = f"""
                    SELECT *
                    FROM Customers
                    WHERE Customers.country LIKE '%{country}%'
                    """
        cursor = Connection.conn.execute(command)
        customers_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(customers_db)
        for customer in customers_db:
            customer2 = Customer(customer[1], customer[2], customer[3], customer[4], customer[5],
                                 customer[6], customer[7], customer[8])
            customer2.display_customer_by_country(customer2.lastName, customer2.firstName,
                                                  customer2.city, customer2.country)

    # Lister les clients par leur date de naissance
    def _display_customers_by_year_of_birth_repo(self):
        try:
            year_of_birth = int(input("Display customers by their year of birth: "))
        except ValueError as erreurDeValeur:
            print("Please enter an integer.", file=sys.stderr)
            print(erreurDeValeur.__doc__)
            sys.exit()
        command = f"""
                    SELECT *
                    FROM Customers
                    WHERE Customers.year_of_birth={year_of_birth}
                    """
        cursor = Connection.conn.execute(command)
        customers_db = cursor.fetchall()
        print(f"Customer(s) born in {year_of_birth}:")
        CountOfDatabase.count_of_database_method(customers_db)
        for customer in customers_db:
            print(f"{customer[2]} {customer[1].upper()} in {customer[4]}, {customer[5]}.")
