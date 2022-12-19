#
# import sys
# import subprocess
#
# # implement pip as a subprocess:
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
# 'pymongo'])
#
from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://ht2568:ht2568columbia@cluster0.om7aato.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial

    item_2 = {
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    }

    dbname = client['update']
    collection_name = dbname['updateHistory']
    collection_name.insert_one(item_2)

    # return client['updateHistory']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    get_database()
