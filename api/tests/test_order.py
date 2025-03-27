import unittest
from fastapi.testclient import TestClient
from api.order import app
class TestAPI(unittest.TestCase):

    def test_add_order(self):
        """
        test api which adds new order
        """
        client = TestClient(app)
        response = client.post("/orders",json = {"item_name":"Sandwich","quantity":1})
        assert response.status_code == 201
        assert response.json() == {"message": {"item_name":"Sandwich","quantity":1}}
    
    def test_get_order_status(self):
        """test api which help us to get status of a particular order"""
        client = TestClient(app)
        order_id = 1
        expected_status ="Processing"
        #mock a store: it contain 1 food item, its id be 1 and let its status be processing
        
        response = client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        assert response.json() == {"Status": expected_status}

    def test_update_order(self):
        """test api which updates an order(change item only)"""
        client = TestClient(app)
        order_id = 1
        response = client.put(f"/orders/{order_id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"message":"updated"})

    def test_cancel_order(self):
        """cancel an order"""
        client = TestClient(app)
        order_id = 1
        response = client.delete(f"/orders/{order_id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"message":"order cancelled"})