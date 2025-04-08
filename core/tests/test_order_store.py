from unittest.mock import patch
import unittest
from core.data_modeling import Item,Order
from core.order_store import OrderStore
import json
from uuid import UUID

from core.data_modeling import Status
class TestOrderStore(unittest.TestCase):
    
    @patch("core.order_store.uuid.uuid4", return_value = UUID("edcf6271-a213-45ea-a851-82af8771f809"))
    @patch("core.order_store.redis_client")
    def test_add(self,mock_redis,mock_uuid):
        """
        testing add function if OrderStore class
        """
        mock_redis.hset.return_value = 1
        obj = OrderStore()
        order = Item(name="sandwich",quantity=2)
        customer_order = Order(customer_name="parvathy",orders=[order],status=Status.PENDING, delivery_person="Bob")
        self.assertEqual(obj.add_order(customer_order),
                         Order(id="edcf6271-a213-45ea-a851-82af8771f809", 
                               customer_name='parvathy',
                               orders=[Item(name='sandwich', quantity=2)],
                               status='PENDING',
                               delivery_person='Bob')
                        )

    @patch("core.order_store.redis_client")
    def test_get_order_by_id(self,mock_redis):
        """
        testing get_order_by_id function if OrderStore class
        """
        dummy_data = {  "id": "5e1a1160-a45d-4a22-bc47-93a4b1d75e63",
                        "customer_name": "parvathy",
                        "orders": [{"name": "sandwich", "quantity": 2}],
                        "status": "PENDING",
                        "delivery_person": "Bob"
                    }
        mock_redis.hget.return_value = json.dumps(dummy_data).encode("utf-8")
        obj = OrderStore()
        result = obj.get_order_by_id("5e1a1160-a45d-4a22-bc47-93a4b1d75e63")
        self.assertEqual(result, dummy_data)

    @patch("core.order_store.redis_client")
    def test_update_order(self,mock_redis):
        obj = OrderStore()
        mock_redis.hset.return_value = 1
        updated_orders = [Item(name="ice cream",quantity=1),Item(name="pizza",quantity=12)]

        mock_redis.hget.return_value = {  "id": "5e1a1160-a45d-4a22-bc47-93a4b1d75e63",
                        "customer_name": "parvathy",
                        "orders": updated_orders,
                        "status": "PENDING",
                        "delivery_person": "Bob"
                    }
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        self.assertEqual(obj.update_order(order_id,updated_orders),
                         { "id": "5e1a1160-a45d-4a22-bc47-93a4b1d75e63",
                        "customer_name": "parvathy",
                        "orders": updated_orders,
                        "status": "PENDING",
                        "delivery_person": "Bob"
                    })

    @patch("core.order_store.redis_client")
    def test_delete_order_successful(self,mock_redis):
        obj = OrderStore()
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        mock_redis.hdel.return_value = 1
        self.assertEqual(obj.delete_order(order_id),1)

    @patch("core.order_store.redis_client")
    def test_get_all(self,mock_redis):
        """
        Test for function which returns all the details from redis with key = customer_store.
        """
        mock_redis.hgetall.return_value = {"dummy-key":"dummy-value"}
        obj = OrderStore()
        self.assertEqual(obj.get_all("customer_store"),{"dummy-key":"dummy-value"})