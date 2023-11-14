from pymongo import MongoClient
from datetime import datetime
MONGODB_URI = "mongodb+srv://myAtlasDBUser:hxEWomfq3gF99ec2@myatlasclusteredu.ncukges.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(MONGODB_URI)

db = client.library

books_collection=db.books

new_books=[]

while True:
    new_book = {}
    new_book['_id'] = int(input('Enter _id : \n'))
    new_book['name'] = input('Enter Book name:\n')
    new_book['ISBN'] = input('Enter ISBN:\n')
    new_book['author'] = input('Enter author\'s name:\n')
    new_book['year'] = int(input('Enter Published Year:\n'))
    new_book['downloads'] = 0
    new_book['last_modified'] = datetime.utcnow()
    new_books.append(new_book)
    stats=input("Insert another? Y/N\n")
    if stats == "N":
        print("Exiting the loop...")
        break
    elif stats=="Y":
        continue

insert=input("You want to insert the document? Y/N\n")
if insert=='Y':
    books_collection.insert_many(new_books)
    print("Insert Operation Successful!")
    client.close()
else:
    client.close()
