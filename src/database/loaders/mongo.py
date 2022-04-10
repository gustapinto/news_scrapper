from os import getenv

from pymongo import MongoClient

from src.interfaces.loader import DatabaseLoader


class MongoLoader(DatabaseLoader):
    def __init__(self):
        self.database_name = getenv('MONGO_DATABASE')
        self.connection_string = getenv('DB_CONNECTION_STRING')

        self.client = self.connect()

    def connect(self) -> MongoClient:
        return MongoClient(self.connection_string)

    def load(self, collection: str, data: list[dict]):
        database = self.client[self.database_name]
        collection = database[collection]

        collection.insert_many(data)
