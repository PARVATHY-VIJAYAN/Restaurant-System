"""
A Module for testing the API calls of order.
"""
from unittest.mock import patch 
import unittest
from fastapi.testclient import TestClient
from api.order import app
from uuid import UUID

class TestAPI(unittest.TestCase):
    @patch("core.order_store.uuid.uuid4", return_value = UUID("edcf6271-a213-45ea-a851-82af8771f809"))   
    @patch("core.order_store.redis_client")
    def test_add_order(self, mock_redis, mock_uuid):
        """
        Test the /orders POST endpoint for adding a new order.
        Mocked redis hset function and uuid.
        """
        mock_redis.hset.return_value = 1
        client = TestClient(app)
        response = client.post("/orders", json={"customer_name": "parvathy",
                                                "orders": [
                                                            {"name": "sandwich", "quantity": 1},
                                                            {"name": "burger", "quantity": 2}
                                                          ],
                                                "delivery_person": "Bob"})
        assert response.status_code == 201
        assert response.json().get("order")["id"] == "edcf6271-a213-45ea-a851-82af8771f809"

    @patch("core.order_store.uuid.uuid4",return_value = UUID("5e1a1160-a45d-4a22-bc47-93a4b1d75e63"))
    @patch("core.order_store.redis_client")
    @patch("core.order_store.OrderStore.get_all",return_value =["5e1a1160-a45d-4a22-bc47-93a4b1d75e63"])
    def test_get_order_by_id_successfull(self,mock_redis,mock_get_all,mock_uuid):
        """
        Test the /orders/order-id GET endpoint for getting a particular order successfully
        """
        client = TestClient(app)
        
        mock_redis.hget.return_value = b'{"customer_name": "lakshmi", "orders": [{"name": "sandwich", "quantity": 2}], "status": "PENDING", "delivery_person": "Bob"}'
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        response = client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        self.assertEqual(response.json().get("message"),"Data retrived successfully")

    @patch("core.order_store.uuid.uuid4",return_value = UUID("5e1a1160-a45d-4a22-bc47-93a4b1d75e63"))
    @patch("core.order_store.redis_client")
    @patch("core.order_store.OrderStore.get_all",return_value =["5e1a1160-a45d-4a22-bc47-93a4b1d75e63"])
    def test_get_order_by_id_fail(self,mock_redis,mock_get_all,mock_uuid):
        """
        Test the /orders/order-id GET endpoint for getting a particular order successfully
        """
        client = TestClient(app)
        mock_redis.hget.return_value = b'{"customer_name": "lakshmi", "orders": [{"name": "sandwich", "quantity": 2}], "status": "PENDING", "delivery_person": "Bob"}'
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e61"
        response = client.get(f"/orders/{order_id}")
        assert response.json()['detail'] == "ID not found"
        assert response.status_code == 404
        
        
    
    @patch("core.order_store.redis_client")
    def test_update_order(self,mock_redis):
        """
        Test the /orders/order-id PATCH endpoints which will updates an order(change item only)
        """
        client = TestClient(app)
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        response = client.patch(url=f"/orders/{order_id}",json={"name": "sandwich", "quantity": 2})
        mock_redis.hset.return_value = 1
        self.assertEqual(response.status_code,200)
        assert response.json() =={"message": "Order updated successfully", "order": {"name": "sandwich", "quantity": 2}}
    
    @patch("core.order_store.redis_client")
    def test_cancel_order(self,mock_redis):
        """
        Test the /orders/order-id DELETE endpoint for cancel an order
        """
        client = TestClient(app)
        order_id = "5e1a1160-a45d-4a22-bc47-93a4b1d75e63"
        mock_redis.hdel.return_value = 1
        response = client.delete(f"/orders/{order_id}")
        self.assertEqual(response.status_code,204)