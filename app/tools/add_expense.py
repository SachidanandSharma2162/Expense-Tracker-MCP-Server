from datetime import datetime
from typing import Optional

from fastmcp import FastMCP
from pydantic import BaseModel

from app.models.expense import ExpenseCreate, Category, ExpenseResponse, PaymentMethod
from app.services.expense_service import expense_service

def register_add_expense_tool(mcp: FastMCP):
    """
    Register the add_expense MCP tool.
    """

    @mcp.tool
    def add_expense(
        title: str,
        amount: float,
        category: Category,
        payment_method: PaymentMethod,
        notes: str = "",
        date: Optional[str] = None,
    ) -> dict:
        """
    Add a new expense.

    Use this tool whenever the user wants to record a purchase,
    payment, bill, or any money spent.
    """
        expense_date = datetime.now()

        if date:
            try:
                expense_date = datetime.fromisoformat(date)
            except ValueError:
                raise ValueError(
                    "Date must be in ISO format (YYYY-MM-DD)"
                )
        expense = ExpenseCreate(
            title=title,
            amount=amount,
            category=category,
            payment_method=payment_method,
            notes=notes,
            date=expense_date,
        )

        result = expense_service.add_expense(expense)

        return {"success": True,"message": "Expense added successfully."}