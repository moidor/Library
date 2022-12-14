# On importe ici la classe CustomerRepository comme un objet et non un module
from src.people.repositories.CustomerRepository import CustomerRepository


class CustomerService(CustomerRepository):
    def search_a_customer_by_name_service(self):
        self._search_a_customer_by_name_repo()

    def display_every_customer_service(self):
        self._display_every_customer_repo()

    def display_customers_by_city_service(self):
        self._display_customers_by_city_repo()

    def display_customers_by_country_service(self):
        self._display_customers_by_country_repo()

    def display_customers_by_year_of_birth_service(self):
        self._display_customers_by_year_of_birth_repo()
