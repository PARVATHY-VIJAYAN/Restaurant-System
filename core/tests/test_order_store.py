from unittest.mock import patch 
import unittest
from core.data_modeling import CustomerOrder,Order
from core.order_store import OrderStore
class TestOrderStore(unittest.TestCase):

    @patch("core.order_store.redis_client")
    def test_add(self,mock_redis):
        """
        testing add function if OrderStore class
        """
        mock_redis.hset.return_value = 1
        obj = OrderStore()
        #dummy values
        order = Order(order_name="sandwich",quantity=2)
        customer_order = CustomerOrder(order_id=1,customer_name="parvathy",orders=[order],status="new",delivery_person="Bob")
        self.assertEqual(obj.add_order(customer_order),1)
    
    @patch("core.order_store.redis_client")
    def test_get_status(self,mock_redis):
        """
        testing get_status function if OrderStore class
        """
        mock_redis.hget.return_value = b'{"customer_name": "parvathy", "orders": [{"order_name": "sandwich", "quantity": 2}], "status": "new", "delivery_person": "Bob"}'
        obj = OrderStore()
        self.assertEqual(obj.get_status(1),"new")
    
    
    @patch("core.order_store.redis_client")
    def test_update_order(self,mock_redis):
        obj = OrderStore()
        mock_redis.hset.return_value = 1
        updated_orders = [Order(order_name="ice cream",quantity=1),Order(order_name="pizza",quantity=12)]
        order_id = 1
        self.assertEqual(obj.update_order(order_id,updated_orders),1)
    
    @patch("core.order_store.redis_client")
    def test_delete_order_successful(self,mock_redis):
        obj = OrderStore()
        order_id = 1
        mock_redis.hdel.return_value = None
        self.assertEqual(obj.delete_order(order_id),"deleted")
        