import unittest
from fastapi.testclient import TestClient
from api.inventory import app

class TestInventoryAPI(unittest.TestCase):
    def test_inventory_add(self):
        client = TestClient(app)
        response = client.post("/inventory/replenish",json ={})
        assert response.status_code == 200
        assert response.json() == {"message": {"created"}}
    