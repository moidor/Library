class Order:
    def __init__(self, number, date):
        self.number = number,
        self.date = date

    def order_introduction(self, number, date, customer_firstname, customer_lastname, seller, book):
        text = f"""
        Summary of your order
            Order n°{number}:
                Customer name: {customer_firstname} {customer_lastname.upper()}
                Title of the book: "{book.upper()}"
                Date of order: {date}
                Seller: {seller}
        """
        # text = f"The order n°{number} of the book \"{book.upper()}\" has been done on {date} " \
        #        f"by {customer_firstname} {customer_lastname.upper()} at {seller}. "
        print(text)
        return text
