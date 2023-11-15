from pymongo import MongoClient
import keyboard
from datetime import datetime
import json

# Read the configuration file
with open('.\config.json', 'r') as config_file:
    config_data = json.load(config_file)

# Access the MongoDB URI
MONGODB_URI = config_data['mongoURI']

client=MongoClient(MONGODB_URI)
for db_name in client.list_database_names():
    print(db_name)

client.close()