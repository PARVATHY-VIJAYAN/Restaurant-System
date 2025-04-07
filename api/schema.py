from pydantic import BaseModel, Field
from core.data_modeling import Item
from typing import List,Literal,Dict

class OrderRequest(BaseModel):
    customer_name: str
    orders: List[Item]
    status: Literal['PENDING', 'IN PROGRESS', 'COMPLETED']
    delivery_person: str

class ReplenishRequest(BaseModel):
    items: Dict[str, int]