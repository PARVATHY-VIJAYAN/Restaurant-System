import unittest
from order import Order
class TestAPI(unittest.TestCase):

    def test_set_all(self):
        order_obj = Order("burger",2)
        order_obj.set_all("sandwich",2)
        self.assertEqual(order_obj.get(),{"name":"sandwich","quantity":2,"status":"new"})

    def test_get(self):
        order_obj = Order("sandwich",1)
        self.assertEqual(order_obj.get(),{"name":"sandwich","quantity":1,"status":order_obj.status})

    def test_get_status(self):
        order_obj = Order("sandwich",1)
        self.assertEqual(order_obj.get_status(),"new")

    def test_set_status(self):
        order_obj = Order("sandwich",1)
        self.assertEqual(order_obj.get_status(),"new")
        order_obj.set_status("inprocess")
        self.assertEqual(order_obj.get(),{"name":"sandwich","quantity":1,"status":order_obj.status})




if __name__ == "__main__":
    unittest.main()