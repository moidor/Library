import sqlite3


class Connection:
    # def __init__(self,
    #              command,
    #              conn=sqlite3.connect("C:\\Users\\Cham\\PycharmProjects\\Library\\src\\database\\database.sqlite3")):
    #     self.conn = conn.execute(command)

    conn = sqlite3.connect("C:\\Users\\Cham\\PycharmProjects\\Library\\src\\database\\database.sqlite3")

