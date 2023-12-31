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
book_id= { "_id" : 234}

#-------------------
book_update={"$set":{"author":"Carol Susan Dweck","last_modified":datetime.utcnow()}}
result=books_collection.update_one(book_id, book_update)

#### update many
# book_filter={"year":{"$gt":2000}}
# book_update={"$set":{"century":"21st Century"}}
# result=books_collection.update_many(book_filter, book_update)


#-------------------print the count of updated document-------------------
print("Documents updated!\n",str(result.modified_count))
print("----------")

pprint.pprint(books_collection.find_one(book_id))

client.close()