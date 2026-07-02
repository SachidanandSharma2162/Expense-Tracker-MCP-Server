from datetime import datetime

from app.database.counters import counter
from app.database.expense_repository import expense_repository
from app.models.expense import ExpenseCreate, ExpenseUpdate

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
    
    def list_expenses(self):
        return self.repo.get_all()
    
    def get_expense(self, expense_id: str):
        return self.repo.get_by_expense_id(expense_id)
    
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