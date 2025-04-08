from typing import Optional
from datetime import date
from typing import Literal
from pydantic import BaseModel,UUID4,Field
from uuid import uuid4

class IngredientName:
    SUGAR = "Sugar"
    SALT = "Salt"
    FLOUR = "Flour"
    BUTTER = "Butter"

class Status:
    PENDING = "PENDING"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"

class Item(BaseModel):
    """
        -> name : name of an item
        -> quantity: an integer number showing how many ordered items the user needs. 
    """
    name : str
    quantity : int

class Ingredient(BaseModel):
    """
        -> name : (str) name of an Ingredient
        -> quantity : (int) number of ingredients
        -> expiry_date : (date) date in which the ingredient get expire. (yyyy-mm-dd)
    """
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
    id: Optional[UUID4] = Field(default_factory=uuid4)
    customer_name: str
    orders: list[Item]
    status: Literal[Status.PENDING, Status.IN_PROGRESS, Status.COMPLETED] = Status.PENDING
    delivery_person: str