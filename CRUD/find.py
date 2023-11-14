from pymongo import MongoClient
import pprint
import keyboard
from datetime import datetime
MONGODB_URI = "mongodb+srv://myAtlasDBUser:hxEWomfq3gF99ec2@myatlasclusteredu.ncukges.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(MONGODB_URI)

db = client.library

books_collection=db.books
book_id= { "_id" : 231}
result=books_collection.find_one(book_id)
pprint.pprint(result)
print("----------")
cursor=books_collection.find({"year":{"$gt":2000}}).sort("year",1)
for doc in cursor:
    pprint.pprint(doc)

client.close()