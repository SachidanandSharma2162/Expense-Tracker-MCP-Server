from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class Category(str, Enum):
    FOOD = "Food"
    TRAVEL = "Travel"
    SHOPPING = "Shopping"
    BILLS = "Bills"
    ENTERTAINMENT = "Entertainment"
    HEALTH = "Health"
    EDUCATION = "Education"
    RENT = "Rent"
    INVESTMENT = "Investment"
    OTHER = "Other"


class PaymentMethod(str, Enum):
    CASH = "Cash"
    UPI = "UPI"
    CARD = "Card"
    BANK = "Bank"

class ExpenseBase(BaseModel):
    """
    Base model containing common expense fields.
    """

    title: str = Field(..., min_length=1, max_length=100)

    amount: float = Field(..., gt=0)

    category: Category
    
    payment_method: PaymentMethod

    notes: Optional[str] = ""

    date: datetime = Field(default_factory=datetime.now)


class ExpenseCreate(ExpenseBase):
    """
    Model used when creating an expense.
    """

    pass


class ExpenseUpdate(BaseModel):
    """
    Model used when updating an expense.
    """

    title: Optional[str] = Field(default=None, min_length=1, max_length=100)

    amount: Optional[float] = Field(default=None, gt=0)

    category: Optional[str] = None

    payment_method: Optional[str] = None

    notes: Optional[str] = None

    date: Optional[datetime] = None


class ExpenseResponse(ExpenseBase):
    """
    Model returned from the database.
    """

    expense_id: str

    created_at: datetime

    updated_at: datetime