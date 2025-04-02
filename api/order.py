from fastapi import FastAPI, Request
from api.schema import OrderRequest
from core.data_modeling import CustomerOrder, Order
from core.order_store import OrderStore

app = FastAPI()

@app.post("/orders", status_code=201)
async def add_order(request: OrderRequest):
    ordered_item_list = []
    for order in request.orders:
        ordered_item_list.append(
            Order(order_name=order.order_name, quantity=order.quantity)
        )
    order = CustomerOrder(order_id=request.order_id,  customer_name=request.customer_name, orders=ordered_item_list, status=request.status, delivery_person=request.delivery_person, )
    order_store = OrderStore()
    order_store.add_order(order)
    return {"message": order}


@app.get("/orders/{order_id}")
async def get_order_status(order_id: int):
    """
    api call for getting the status of an order
    """
    order_store = OrderStore()
    return {"Status": order_store.get_status(order_id)}


@app.put("/orders/{order_id}")
async def update_order_successful(request:Request, order_id: int):
    """
    data contain updated orders in {order_itemname: qtuantity,...} format
    """
    updated_orders = await request.json()
    order_store = OrderStore()
    order_store.update_order(order_id,updated_orders)
    return {"message": "updated"}


@app.delete("/orders/{order_id}")
async def get_order_cancel_successful(order_id: int):
    order_store = OrderStore()
    order_store.delete_order(order_id)
    return {"message": "order cancelled"}
