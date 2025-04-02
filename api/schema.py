from pydantic import BaseModel, Field
from core.data_modeling import Order
from typing import List
class OrderRequest(BaseModel):
    order_id :int 
    customer_name: str 
    orders: List[Order] 
    status: str 
    delivery_person: str 