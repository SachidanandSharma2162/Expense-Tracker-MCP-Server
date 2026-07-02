from pymongo import ReturnDocument

from app.config import settings
from app.database.connection import mongodb


class Counter:
    """
    Handles sequential ID generation for collections.
    """

    def __init__(self):
        db = mongodb.get_database()
        self.collection = db[settings.counter_collection]

    def get_next_expense_id(self) -> str:
        counter = self.collection.find_one_and_update(
            {"_id": "expenseId"},
            {"$inc": {"sequence": 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

        sequence = counter["sequence"]

        return f"EXP{sequence:04d}"


counter = Counter()