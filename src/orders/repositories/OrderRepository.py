import sys
from src.database.Connection import Connection
from src.models.Order import Order
from src.interfaces.CountOfDatabase import CountOfDatabase
from src.streams.OrderBill import OrderBill, create_order_bill
from src.streams.PDF_bill import create_order_bill_pdf


class OrderRepository(Connection):
    # Rechercher une commande par son numéro (id)
    def _search_an_order_by_number_repo(self):
        number = input("Search an order by number: ")
        number_int = int(number)
        command = f"""
                SELECT Orders.id, Orders.orderDate, Customers.firstname, Customers.lastname, Sellers.name, Books.title
                FROM (((Orders
                INNER JOIN Customers ON Orders.CustomerID = Customers.id)
                INNER JOIN Sellers ON Orders.id = Sellers.id)
                INNER JOIN Books on Orders.id = Books.id)
                WHERE Orders.id = '{number_int}';
                """
        cursor = Connection.conn.execute(command)
        orders_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(orders_db)
        for order in orders_db:
            order_obj = Order(order[0], order[1])
            # Unpacking de tuple : le premier argument permet de convertir le numéro de commande en string
            order_id, order_date, customer_firstname, customer_lastname, seller, book = \
                order_obj.number[0], order_obj.date, order[2], order[3], order[4], order[5]
            order_bill_text = order_obj.order_introduction(
                order_id, order_date, customer_firstname, customer_lastname.upper(), seller, book)

            choice_print = input(f"Do you want to download the bill n°{order_id} ? \n"
                                 f"Y = Yes or N = No : ")
            if choice_print.upper() == "Y":
                # create_order_bill(order_bill_text, order_id, customer_lastname, order_date)
                create_order_bill_pdf(order_bill_text, order_id, customer_lastname, order_date)
            elif choice_print.upper() == "N":
                break
