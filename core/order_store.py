from core.redis_client import redis_client
from core.data_modeling import CustomerOrder,Order
import json
from dataclasses import asdict

class OrderStore:
    """
    OrderStore class conatin redis datastore 
    """
    def __init__(self):
        self.redis_data_store = redis_client
    
    def add_order(self, order:CustomerOrder)->int:
        """
        Add customer order to Redis.
        """
        dict_orders = []
        for i in order.orders:
            dict_orders.append(asdict(i))
        
        customer_order_dict = {
            order.order_id : json.dumps({
                "customer_name": order.customer_name,
                "orders": dict_orders,  
                "status": order.status,
                "delivery_person": order.delivery_person
            })
        }
        return self.redis_data_store.hset("customer_order", mapping=customer_order_dict)
    
    def get_status(self,order_id: int):
        data = self.redis_data_store.hget("customer_order",order_id)
        return json.loads(data.decode("utf-8"))["status"]
    
    def update_order(self,order_id: int, updated_orders: dict):
        return self.redis_data_store.hset("customer_order","orders",updated_orders)
    
    def delete_order(self,order_id:int):
        self.redis_data_store.hdel("customer_order",order_id)
        return "deleted"
