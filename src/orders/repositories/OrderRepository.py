import sys
from src.database.Connection import Connection
from src.models.Order import Order
from src.interfaces.CountOfDatabase import CountOfDatabase
from src.streams.DOCX_bill import create_order_bill_docx
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
                WHERE Orders.id = {number_int};
                """
        cursor = Connection.conn.execute(command)
        orders_db = cursor.fetchall()
        CountOfDatabase.count_of_database_method(orders_db)
        # Itération pour retrouver la facture selon son numéro (id)
        for order in orders_db:
            order_obj = Order(order[0], order[1])
            # Unpacking du tuple : le premier argument permet de convertir le numéro de commande en string
            order_id, order_date, customer_firstname, customer_lastname, seller, book = \
                order_obj.number[0], order_obj.date, order[2], order[3], order[4], order[5]
            # Appel de la fonction de l'objet "Order"
            order_bill_text = order_obj.order_introduction(
                order_id, order_date, customer_firstname, customer_lastname.upper(), seller, book)

            choice_print = input(f"Do you want to download the bill n°{order_id} ? \n"
                                 f"Y = Yes or N = No : ")
            if choice_print.upper() == "Y":
                bill_format = input(f"In which format do you want to print the bill ? \n1 = DOCX or 2 = PDF : ")
                if bill_format == "1":
                    create_order_bill_docx(order_bill_text, order_id, customer_lastname, order_date)
                elif bill_format == "2":
                    create_order_bill_pdf(order_id, order_date, customer_firstname, customer_lastname, seller, book)
            elif choice_print.upper() == "N":
                break
