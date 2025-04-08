"""
Module which defines api calls for add,update, delete and get orders 
"""
from pydantic import UUID4
from fastapi import FastAPI, Request, HTTPException
from api.schema import OrderRequest
from core.order_store import OrderStore

app = FastAPI()

@app.post("/orders", status_code=201)
async def add_order(request: OrderRequest)->dict:
    """
    api call for adding an new order
    """
    order_data ={
                  "customer_name":request.customer_name,
                  "orders":request.orders,
                  "delivery_person":request.delivery_person
                }
    order_store = OrderStore()
    order = order_store.add_order(order_data)
    return {"message": "order created successfully",
            "order":order.model_dump()
            }

@app.get("/orders/{order_id}")
async def get_order_by_id(order_id: UUID4):
    """
    api call for getting the status of an order
    """
    order_store = OrderStore()
    if str(order_id) in order_store.get_all("customer_store"):
        return {"message":"Data retrived successfully",
                "order":order_store.redis_data_store.hget("customer_order",order_id) ,
                "_link":{"self": {"href":f"orders/{order_id}"},
                        "update":{"href" : f"orders/{order_id}"},
                        "delete": {"href": f"orders/{order_id}"}
                        }
                }
    else:
        raise HTTPException(status_code=404, detail="ID not found")

#PATCH → used when u modify part of an existing resource (partial update)
@app.patch("/orders/{order_id}")
async def update_order_successful(request:Request, order_id: UUID4):
    """
    data contain updated orders in {order_itemname: qtuantity,...} format
    """
    updated_orders = await request.json()
    order_store = OrderStore()
    order_store.update_order(order_id,updated_orders)
    return {"message":"Order updated successfully",
            "order":updated_orders
            }

@app.delete("/orders/{order_id}",status_code=204)
async def get_order_cancel_successful(order_id: UUID4):
    """
    api call for delete an order using order id.
    """
    order_store = OrderStore()
    order_store.delete_order(order_id)