from datetime import datetime
from typing import Optional

from app.database.counters import counter
from app.database.expense_repository import expense_repository
from app.models.expense import Category, ExpenseCreate, ExpenseUpdate, PaymentMethod

class ExpenseService:

    def __init__(self):
        self.repo = expense_repository
        self.counter = counter

    def add_expense(self, expense: ExpenseCreate):
        expense_dict = expense.model_dump()
        expense_dict["expense_id"] = self.counter.get_next_expense_id()
        now = datetime.now()
        expense_dict["created_at"] = now
        expense_dict["updated_at"] = now
        self.repo.create(expense_dict)
        return expense_dict
    
    def list_expenses(self,category: Optional[Category] = None,limit: Optional[int] = None,):
        return self.repo.get_all(
            category=category.value if category else None,
            limit=limit,
        )
    
    def find_expenses(
    self,
    title: Optional[str] = None,
    category: Optional[Category] = None,
    amount: Optional[float] = None,
    payment_method: Optional[PaymentMethod] = None,
    expense_date: Optional[datetime] = None,
):
        """
        Find expenses using the supplied filters.
        """
    
        return self.repo.find_expenses(
            title=title,
            category=category,
            amount=amount,
            payment_method=payment_method,
            expense_date=expense_date,
        )
    
    def delete_expense(self, expense_id: str):
        return self.repo.delete(expense_id)
    
    def update_expense(self,expense_id: str,expense: ExpenseUpdate):
        updates = expense.model_dump(
            exclude_none=True
        )
    
        updates["updated_at"] = datetime.now()
    
        return self.repo.update(
            expense_id,
            updates
        )
    
expense_service = ExpenseService()