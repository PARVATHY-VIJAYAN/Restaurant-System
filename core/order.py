"""Order class to mangae order related functionalities"""
class Order:
    """
    
    class Order
        Attributes: 
            -> order_name : name of the ordered item
            -> quantity : an integer number showing how many ordered item user needs. 
            -> status : status of the order. (new(in begining), inprocess, delivered)
        Methods:
            -> set_all()
            -> set_status()
            -> 
            -> get()
            -> get_status()
            ->

    """
    def __init__(self,name:str = "" ,quantity:int = 0, status:str = "new"):
        self.order_name = name
        self.quantity = quantity
        self.status = status

    def set_all(self, name:str, quantity:int, status="new")-> dict:
        """ Setting order details """
        self.order_name = name
        self.quantity = quantity
        self.status = status
        return self.get()
    
    def get_status(self)->str:
        """ To get the Status of ordered food """
        return self.status

    def get(self)->dict:
        """ To get all the details of an order """
        return {"name": self.order_name, 
                "quantity":self.quantity, 
                "status":self.status
                }

    def set_status(self,update_status:str):
        """ To set the Status of an ordered food """
        self.status = update_status
        return self.get()
    
    