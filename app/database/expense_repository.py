from datetime import datetime, time

from pymongo.collection import Collection

from app.config import settings
from app.database.connection import mongodb
from typing import Optional

from app.models.expense import Category

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
    
    def find_expenses(
    self,
    title: Optional[str] = None,
    category: Optional[Category] = None,
    amount: Optional[float] = None,
    payment_method=None,
    expense_date: Optional[datetime] = None,
):
        """
        Find expenses matching the given filters.
        """
    
        query = {}
    
        if title:
            query["title"] = {
                "$regex": f"^{title}$",
                "$options": "i"
            }
    
        if category:
            query["category"] = category.value
    
        if amount is not None:
            query["amount"] = amount
    
        if payment_method:
            query["payment_method"] = payment_method.value
    
        if expense_date:
            start = datetime.combine(expense_date.date(), time.min)
            end = datetime.combine(expense_date.date(), time.max)
    
            query["date"] = {
                "$gte": start,
                "$lte": end,
            }
    
        return list(
            self.collection.find(
                query,
                {"_id": 0}
            )
        )
    
    def update_by_expense_id(
    self,
    expense_id: str,
    updates: dict,
) -> bool:
        """
        Update an expense using its expense_id.
        """
    
        result = self.collection.update_one(
            {"expense_id": expense_id},
            {"$set": updates},
        )
    
        return result.modified_count > 0

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