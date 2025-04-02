from unittest.mock import patch 
import unittest
from fastapi.testclient import TestClient
from api.order import app
import json
from core.order_store import OrderStore

class TestAPI(unittest.TestCase):
    @patch("core.order_store.redis_client")
    def test_add_order(self,mock_redis):
        """
        test api which adds new order
        """
        mock_redis.hset.return_value =1
        client = TestClient(app)
        response = client.post("/orders",json ={"order_id":1,"customer_name":"parvathy","delivery_person":"Bob","orders":[{"order_name":"sandwich","quantity":1},{"order_name":"burger","quantity":2}],"status":"1"})
        assert response.status_code == 201
        assert response.json() == {"message": {"order_id":1,"customer_name":"parvathy","delivery_person":"Bob","orders":[{"order_name":"sandwich","quantity":1},{"order_name":"burger","quantity":2}],"status":"1"}}
    
    @patch("core.order_store.redis_client")
    def test_get_order_status_successful(self,mock_redis):
        """
        test api which help us to get status of a particular order
        """
        client = TestClient(app)
        mock_redis.hget.return_value = b'{"customer_name": "parvathy", "orders": [{"order_name": "sandwich", "quantity": 2}], "status": "new", "delivery_person": "Bob"}'
        order_id = 1
        expected_status ="new"
        response = client.get(f"/orders/{order_id}")
        
        assert response.status_code == 200
        assert response.json() == {'Status': expected_status}

    @patch("core.order_store.redis_client")
    def test_update_order(self,mock_redis):
        """
        test api which updates an order(change item only)
        """
        client = TestClient(app)
        order_id = 1
        response = client.put(url=f"/orders/{order_id}",json={})
        mock_redis.hset.return_value = 1
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"message":"updated"})
    
    @patch("core.order_store.redis_client")
    def test_cancel_order(self,mock_redis):
        """cancel an order"""
        client = TestClient(app)
        order_id = 1
        mock_redis.hdel.return_value = 1
        response = client.delete(f"/orders/{order_id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"message":"order cancelled"})