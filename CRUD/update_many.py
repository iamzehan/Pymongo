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

#### update many
book_filter={"year":{"$gt":2000}}
book_update={"$set":{"century":"21st Century","last_modified":datetime.utcnow()}}
result=books_collection.update_many(book_filter, book_update)


#-------------------print the count of updated document-------------------
print("Documents updated!\n",str(result.modified_count))
print("----------")

for doc in books_collection.find(book_filter).sort("year",1):
    pprint.pprint(doc)
    print('\n')

client.close()