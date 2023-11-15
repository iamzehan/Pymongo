from pymongo import MongoClient
import pprint
import keyboard
from datetime import datetime
import json

# Read the configuration file
with open('.\config.json', 'r') as config_file:
    config_data = json.load(config_file)

# Access the MongoDB URI
MONGODB_URI = config_data['mongoURI']

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