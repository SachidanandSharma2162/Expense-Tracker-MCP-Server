from pymongo import MongoClient
from pymongo.database import Database

from app.config import settings


class MongoDB:
    """
    Handles MongoDB connection and provides access
    to the configured database.
    """

    def __init__(self):
        self.client = MongoClient(settings.mongodb_uri)
        self.db: Database = self.client[settings.database_name]

    def get_database(self) -> Database:
        return self.db

    def close(self):
        self.client.close()


# Singleton instance
mongodb = MongoDB()