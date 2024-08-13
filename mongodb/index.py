import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")
db = myClient["test"]
col = db["orders"]

dic = {"name": "IPhone 15 pro max", "price": 2000000.0, "phoneNumber": "+250790104332"}
x = col.insert_one(dic)
print(x)
