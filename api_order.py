from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

@app.post("/orders",status_code=201)
async def add_order(request:Request):
    data = await request.json()

    return {"message": data}

@app.get("/orders/{order_id}")

async def get_order_status(order_id: int):
    
    
    return {"Status": "Processing"}
@app.put("/order/{order_id}")
@app.delete("/orders/{order_id}")
async def get_order_cancel(order_id: int):
    
    
    return {"message": "order cancelled"}
