from fastapi import FastAPI, HTTPException, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from pymongo import MongoClient
import uvicorn
from typing import List, Optional
from database.database import *
from repository.models import *

app = FastAPI(debug=True)

mongo_client = MongoClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)

db = mongo_client[DB_NAME]
collection = db[DB_COLLECTION]


@app.get('/',
         response_description="List All items",
         response_model=List[ItemModel]
         )
def get_items():

    data = []
    for document in collection.find():
        print(document)
        document['_id'] = str(document['_id'])
        data.append(document)

    # return {"items": data}
    return data


@app.post("/add_item",
          response_description="Add Item",
          response_model=ItemModel)
def add_item(new_data: ItemModel = Body(...)):
    item = jsonable_encoder(new_data)
    print(item)
    result = collection.insert_one(item)

    if result.inserted_id:
        # return {"message": "Data inserted successfully"}
        created_item = collection.find_one({"_id": result.inserted_id})
        created_item['_id'] = str(created_item['_id'])
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_item)
    else:
        raise HTTPException(status_code=500, detail="Failed to insert data")


if __name__ == "__main__":
    uvicorn.run(app)
