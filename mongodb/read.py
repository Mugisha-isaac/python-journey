import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")
db = myClient["test"]
col = db["orders"]

# find one document
# x = col.find_one({"name": "IPhone 15 pro max"})
# print(x)

# find all documents

for x in col.find():
    print(x)
