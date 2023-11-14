from pymongo import MongoClient
import keyboard
from datetime import datetime
MONGODB_URI = "mongodb+srv://myAtlasDBUser:hxEWomfq3gF99ec2@myatlasclusteredu.ncukges.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(MONGODB_URI)
for db_name in client.list_database_names():
    print(db_name)

client.close()