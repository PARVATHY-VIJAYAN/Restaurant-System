import json
import uuid
from uuid import UUID
from core.redis_client import redis_client
from core.data_modeling import Order
class OrderStore:
    """
    OrderStore class conatin redis datastore 
    """
    def __init__(self):
        self.redis_data_store = redis_client
 
    def add_order(self, order_data:dict)->Order:
        """
        Add customer order to Redis.
        """
        order = Order.model_validate(order_data)
        order.id = uuid.uuid4()
        customer_order_dict = {str(order.id): order.model_dump_json()}
        self.redis_data_store.hset("customer_order", mapping=customer_order_dict)
        return order
    
    def get_order_by_id(self,order_id: UUID)->dict:
        """
        get all the details of a particular order
        """
        data = self.redis_data_store.hget("customer_order",order_id)
        return json.loads(data.decode("utf-8"))
    
    def update_order(self,order_id: UUID, updated_orders: dict)->dict:
        """
        Update an existing order in the Redis data store.
        """
        self.redis_data_store.hset("customer_order",order_id,updated_orders)
        return self.redis_data_store.hget("customer_order",order_id)
    
    def delete_order(self,order_id:UUID):
        """
        delete an order details from redis.
        """
        return self.redis_data_store.hdel("customer_order",order_id)
    
    def get_all(self,key:str):
        return self.redis_data_store.hgetall("customer_store")
    
