from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import uvicorn
from database.database import *

app = FastAPI(debug=True)

mongo_client = MongoClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)

db = mongo_client[DB_NAME]
collection = db[DB_COLLECTION]


@app.get('/')
def get_items():

    data = []
    for document in collection.find():
        print(document)
        document['_id'] = str(document['_id'])
        data.append(document)

    return {"items": data}


@app.post("/add_item")
def add_item(new_data: dict):
    result = collection.insert_one(new_data)

    if result.inserted_id:
        return {"message": "Data inserted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to insert data")


if __name__ == "__main__":
    uvicorn.run(app)
