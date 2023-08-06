"""
Description:
   make connections with most of nosql DB servers.
"""

def _connect_to_mongodb():
    from pymongo import MongoClient
    CONNECTION_STRING = "mongodb://localhost:27017"
        # "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    try:
        MONGODBCON = MongoClient(CONNECTION_STRING)
    except:
        MONGODBCON = None