from pymongo.collection import Collection

from app.config import settings
from app.database.connection import mongodb


class ExpenseRepository:
    """
    Handles CRUD operations for expenses.
    """

    def __init__(self):
        db = mongodb.get_database()
        self.collection: Collection = db[settings.collection_name]

    def create(self, expense: dict):
        """
        Insert a new expense into MongoDB.
        """
        return self.collection.insert_one(expense)
    
    def get_all(self):
        """
        Return all expenses.
        """
        return list(
            self.collection.find(
                {},
                {"_id": 0}
            )
        )
    
    def get_by_expense_id(self, expense_id: str):
        """
        Return a single expense.
        """
        return self.collection.find_one(
            {"expense_id": expense_id},
            {"_id": 0}
        )
    
    def update(self, expense_id: str, updates: dict):
       """
       Update an existing expense.
       """
       return self.collection.update_one(
           {"expense_id": expense_id},
           {"$set": updates}
       )
    
    def delete(self, expense_id: str):
       """
       Delete an expense.
       """
       return self.collection.delete_one(
           {"expense_id": expense_id}
       )
    
expense_repository = ExpenseRepository()