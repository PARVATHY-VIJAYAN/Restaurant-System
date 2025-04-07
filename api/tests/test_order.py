"""
A Module for testing the API calls of order.
"""
from unittest.mock import patch 
import unittest
from fastapi.testclient import TestClient
from api.order import app
from core.data_modeling import Status

class TestAPI(unittest.TestCase):

    @patch("core.data_modeling.uuid.uuid4",return_value = "edcf6271-a213-45ea-a851-82af8771f809")
    @patch("api.order.add_order",return_value = 1)
    @patch("core.order_store.redis_client")
    def test_add_order(self,mock_redis,mock_add_order,mock_uuid):
        """
        test api which adds new order
        """
        mock_redis.hset.return_value = 1
        client = TestClient(app)
        response = client.post("/orders",json ={"customer_name":"parvathy","delivery_person":"Bob","orders":[{"name":"sandwich","quantity":1},{"name":"burger","quantity":2}],"status":Status.PENDING})
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.json().get("message"),"order created successfully")
        #self.assertEqual(str(response.json().get("order")),{'id': 'b1ef2ec0-883e-43eb-91d9-8c1069176f30', 'customer_name': 'parvathy', 'orders': [{'name': 'sandwich', 'quantity': 1}, {'name': 'burger', 'quantity': 2}], 'status': 'PENDING', 'delivery_person': 'Bob'})


    @patch("core.order_store.redis_client")
    def test_get_order_by_id(self,mock_redis):
        """
        test api which help us to get status of a particular order
        """
        client = TestClient(app)
        mock_redis.hget.return_value = b'{"customer_name": "lakshmi", "orders": [{"name": "sandwich", "quantity": 2}], "status": "PENDING", "delivery_person": "Bob"}'
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        response = client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        self.assertEqual(response.json(), {'message': 'Data retrived successfully', 'order': '{"customer_name": "lakshmi", "orders": [{"name": "sandwich", "quantity": 2}], "status": "PENDING", "delivery_person": "Bob"}'})
    
    @patch("core.order_store.redis_client")
    def test_update_order(self,mock_redis):
        """
        test api which updates an order(change item only)
        """
        client = TestClient(app)
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        response = client.put(url=f"/orders/{order_id}",json={"name": "sandwich", "quantity": 2})
        mock_redis.hset.return_value = 1
        self.assertEqual(response.status_code,200)
        assert response.json() =={'message': 'Order updated successfully', 'order': {'name': 'sandwich', 'quantity': 2}}
    
    @patch("core.order_store.redis_client")
    def test_cancel_order(self,mock_redis):
        """
        cancel an order
        """
        client = TestClient(app)
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        response = client.delete(f"/orders/{order_id}")
        mock_redis.hdel.return_value = 1
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"message": "deleted"})