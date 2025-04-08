from pydantic import BaseModel
from typing import List,Literal,Dict
from core.data_modeling import Item



class OrderRequest(BaseModel):
    customer_name: str
    orders: List[Item]
    status: Literal['PENDING', 'IN PROGRESS', 'COMPLETED'] = "PENDING"
    delivery_person: str

class ReplenishRequest(BaseModel):
    items: Dict[str, int]