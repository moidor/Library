import sqlite3
from src.database.Connection import Connection


class DbBackup(Connection):
    # Sauvegarder la base de données
    def save_database(self):
        input("Press \"Enter\" to save the database: ")
        backup_file = sqlite3.connect('C:\\Users\\Cham\\'
                                      'PycharmProjects\\Library\\src\\database\\backup\\database.sqlite3')
        try:
            Connection.conn.backup(backup_file)
            print("Database backup created.")
        except Exception as exception:
            print(f"Error: {exception}")
        finally:
            Connection.conn.close()
