from pymongo.collection import Collection

from app.config import settings
from app.database.connection import mongodb
from typing import Optional

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
    
    def get_all(self,category: Optional[str] = None,limit: Optional[int] = None,):
        """
        Retrieve expenses with optional filtering.
        """
    
        query = {}
    
        if category:
            query["category"] = category
    
        cursor = (
            self.collection
            .find(query, {"_id": 0})
            .sort("date", -1)
        )
    
        if limit:
            cursor = cursor.limit(limit)
    
        return list(cursor)
    
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
       result= self.collection.delete_one(
           {"expense_id": expense_id}
       )
       return result.deleted_count>0
    
expense_repository = ExpenseRepository()