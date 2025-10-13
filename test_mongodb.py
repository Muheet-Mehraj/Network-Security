import pymongo
from pymongo.errors import ConnectionFailure

# Replace placeholders with your actual credentials
connection_string = "mongodb....."

try:
    client = pymongo.MongoClient(connection_string)
    client.admin.command('ping')
    print(" Successfully connected to MongoDB!")
except ConnectionFailure as e:
    print(f" Could not connect to MongoDB: {e}")
except Exception as e:
    print(f"An error occurred: {e}")    