from src.database.Connection import Connection


def orders_stream(customer_lastname, customer_firstname, seller_name, book_title, date):
    # Création de variables destinées à être modifiées pour l'ajout de l'apostrophe en BDD
    if "'" in book_title or customer_lastname or customer_firstname or seller_name:
        new_customer_lastname = customer_lastname.replace("'", "\'")
        new_customer_firstname = customer_firstname.replace("'", "\'")
        new_seller_name = seller_name.replace("'", "\'")
        new_book_title = book_title.replace("'", "\'")

        # Clés étrangères : si les informations sont renseignées, donc ni null ni une chaîne vide
        if new_customer_lastname and new_customer_firstname and new_seller_name and new_book_title is not None or "":
            # Alors on lance des requêtes SQL dans les tables respectives en vue de récupérer les id nécessaires
            sql_customer_id = f"""
                        SELECT id
                        FROM Customers
                        WHERE lastname='{new_customer_lastname}' AND firstname='{new_customer_firstname}';
                    """
            sql_seller_id = f"""
                        SELECT id
                        FROM Sellers
                        WHERE name='{new_seller_name}';
                    """
            sql_book_title_id = f"""
                        SELECT id
                        FROM Books
                        WHERE title='{new_book_title}';
                    """
            # Exécution des requêtes
            cursor_customer_id = Connection.conn.execute(sql_customer_id)
            customer_id = cursor_customer_id.fetchone()
            cursor_seller_id = Connection.conn.execute(sql_seller_id)
            seller_id = cursor_seller_id.fetchone()
            cursor_book_title_id = Connection.conn.execute(sql_book_title_id)
            book_id = cursor_book_title_id.fetchone()
            print(f"Different ids from DB: Customer: "
                  f"{customer_id[0]}, seller: {seller_id[0]}, book: {book_id[0]}, {date}")
            # Requête d'insertion en BDD des ids des clés étrangères
            command = f"""
                        INSERT INTO Orders (customerId, sellerId, bookId, orderDate)
                        VALUES ({customer_id[0]}, {seller_id[0]}, {book_id[0]}, {date});
                    """
            duplicate_rows_removing = f"""
                                DELETE FROM Orders
                                    WHERE id NOT IN (
                                    Select MIN(id)
                                    from Orders
                                    group by orderDate
                                    );
                                """
            params = customer_id[0], seller_id[0], book_id[0], date
            Connection.conn.execute("INSERT INTO Orders VALUES (NULL, ?, ?, ?, ?)", params)
            # Connection.conn.execute(command)
            Connection.conn.execute(duplicate_rows_removing)
            Connection.conn.commit()
            print(Connection.conn.cursor().rowcount, "Order inserted in the Orders table.")
        # else:
        #     command = f"""
        #                     INSERT INTO Books (title, year, summary, author_id)
        #                     VALUES ("{new_book_title}", {book_year}, "{new_summary}", "NULL");
        #                 """
        #     duplicate_rows_removing = f"""
        #                                 DELETE FROM Books
        #                                     WHERE id NOT IN (
        #                                     Select MIN(id)
        #                                     from Books
        #                                     group by title
        #                                     );
        #                                 """
        #     Connection.conn.execute(command)
        #     Connection.conn.execute(duplicate_rows_removing)
        #     Connection.conn.commit()
        #     print(Connection.conn.cursor().rowcount, "Order inserted in the Orders table.")


class Orders_stream:
    pass
