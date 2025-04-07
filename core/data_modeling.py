import uuid
from dataclasses import dataclass,field
from typing import Dict, Literal
import uuid
from pydantic import BaseModel,UUID4,Field
from datetime import date

class IngredientName:
    SUGAR = "Sugar"
    SALT = "Salt"
    FLOUR = "Flour"
    BUTTER = "Butter"

class Status:
    PENDING = "PENDING"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"

    

@dataclass
class Item:
    """
        -> name : name of an item
        -> quantity: an integer number showing how many ordered items the user needs. 
    """
    name : str
    quantity : int


    
class Ingredient(BaseModel):
    name: str
    quantity: int = Field(ge=0)
    expiry_date: date



class Order(BaseModel):
    """
    class Order
        Attributes: 
            -> id :order id
            -> customer_name : name of the customer
            -> orders : list of ordered item (type = Item)
            -> status : status of the order (restricted the values: 'PENDING', 'IN PROGRESS' , 'COMPLETED')
            -> delivery_person: name of the person who delivers the product"
    """
    id:UUID4 = uuid.uuid4()
    customer_name: str
    orders: list[Item]
    status: Literal[Status.PENDING, Status.IN_PROGRESS, Status.COMPLETED]
    delivery_person: str
