# On importe ici la classe OrderRepository comme un objet et non un module
from src.orders.repositories.OrderRepository import OrderRepository


class OrderService(OrderRepository):
    def search_an_order_by_number_service(self):
        self._search_an_order_by_number_repo()
