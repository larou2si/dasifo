"""
Description:
   make connections with most of nosql DB servers.
"""

# mongoDB
from pymongo import MongoClient
CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
try:
    MONGODBCON = MongoClient(CONNECTION_STRING)
except:
    MONGODBCON = None