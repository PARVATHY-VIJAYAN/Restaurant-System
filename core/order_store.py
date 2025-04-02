from core.redis_client import redis_client
from core.data_modeling import Order
import json
from dataclasses import asdict
from uuid import UUID


class OrderStore:
    """
    OrderStore class conatin redis datastore 
    """
    def __init__(self):
        self.redis_data_store = redis_client
 
    def add_order(self, order:Order)->int:
        """
        Add customer order to Redis.
        """
        dict_orders = []
        for i in order.orders:
            dict_orders.append(asdict(i))
       
        customer_order_dict = {
            order.id : json.dumps({
                "customer_name": order.customer_name,
                "orders": dict_orders,  
                "status": order.status,
                "delivery_person": order.delivery_person
            })
        }
        return self.redis_data_store.hset("customer_order", mapping=customer_order_dict)
    
    def get_order_by_id(self,order_id: UUID):
        data = self.redis_data_store.hget("customer_order",order_id)
        return json.loads(data.decode("utf-8"))
    
    def update_order(self,order_id: UUID, updated_orders: dict):
        self.redis_data_store.hset("customer_order",order_id,updated_orders)
        return self.redis_data_store.hget("customer_order",order_id)
    
    def delete_order(self,order_id:UUID):
        return self.redis_data_store.hdel("customer_order",order_id)
        
    