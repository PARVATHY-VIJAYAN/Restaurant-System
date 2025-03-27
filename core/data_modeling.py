from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    """
        -> order_name : name of the ordered item
        -> quantity: an integer number showing how many ordered items the user needs. 
    """
    order_name : str
    quantity : int
@dataclass
class CustomerOrder:
    """
    class CustomerOrder
        Attributes: 
            -> order_id 
            -> customer_name : name of the customer
            -> orders : list of ordered item (type = Order)
            -> status : status of the order. (new(in beginning), in process, delivered)
            -> delivery_person: name of the person who delivers the product"
    """
    order_id: int
    customer_name: str
    orders: List[Order]
    status: str
    delivery_person: str