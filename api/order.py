import json
from fastapi import FastAPI, Request
from api.schema import OrderRequest
from core.data_modeling import Order
from core.order_store import OrderStore
from core.data_modeling import Status
from uuid import UUID

app = FastAPI()

# @app.post("/orders", status_code=201)
# async def add_order(request: OrderRequest)->dict:

#     order = Order(
#                   customer_name=request.customer_name, 
#                   orders=request.orders,
#                   status= Status.PENDING,
#                   delivery_person=request.delivery_person
#                   )
#     order_store = OrderStore()
#     order_store.add_order(order)
#     return {"message": order.model_dump(exclude={"id"})}


# @app.get("/orders/{order_id}")
# async def get_order_by_id(order_id: UUID):
#     """
#     api call for getting the status of an order
#     """
#     order_store = OrderStore()
#     return order_store.redis_data_store.hget("customer_order",order_id)
        


# @app.put("/orders/{order_id}")
# async def update_order_successful(request:Request, order_id: UUID):
#     """
#     data contain updated orders in {order_itemname: qtuantity,...} format
#     """
#     updated_orders = await request.json()
#     order_store = OrderStore()
#     order_store.update_order(order_id,updated_orders)
#     return {"updated":updated_orders}


@app.delete("/orders/{order_id}")
async def get_order_cancel_successful(order_id: UUID):
    order_store = OrderStore()
    if order_store.delete_order(order_id):
        return {"message": "deleted"}