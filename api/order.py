from fastapi import FastAPI, Request
from core.data_modeling import CustomerOrder,Order
app = FastAPI()

@app.post("/orders",status_code=201)
async def add_order(request:Request):
    ordered_item_list = []
    data = await request.json()
    for name,quantity in data["orders"].items():
        ordered_item_list.append(Order(order_name = name, quantity = quantity))


    order = CustomerOrder(order_id=data["order_id"],
                          customer_name=data["customer_name"], 
                          orders=ordered_item_list,
                          status=data["status"],
                          delivery_person = data["delivery_person"])
    return {"message": data}

@app.get("/orders/{order_id}")
async def get_order_status(order_id: int):
    
    
    return {"Status": "Processing"}

@app.put("/orders/{order_id}")
async def update_order(order_id: int):
    return {"message":"updated"}

@app.delete("/orders/{order_id}")
async def get_order_cancel(order_id: int):
    
    
    return {"message": "order cancelled"}
