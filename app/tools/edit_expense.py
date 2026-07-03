from datetime import datetime
from typing import Optional

from fastmcp import FastMCP

from app.models.expense import (
    Category,
    ExpenseUpdate,
    PaymentMethod,
)
from app.services.expense_service import expense_service


def register_edit_expense_tool(mcp: FastMCP):
    """
    Register the edit_expense MCP tool.
    """

    @mcp.tool
    def edit_expense(
        title: Optional[str] = None,
        category: Optional[Category] = None,
        amount: Optional[float] = None,
        payment_method: Optional[PaymentMethod] = None,
        expense_date: Optional[str] = None,

        new_title: Optional[str] = None,
        new_amount: Optional[float] = None,
        new_category: Optional[Category] = None,
        new_payment_method: Optional[PaymentMethod] = None,
        new_notes: Optional[str] = None,
    ) -> dict:
        """
        Edit an existing expense.
        Update an expense by searching for it.
        The expense can be identified using title,
        category, amount, payment method and/or date.
        """

        updates = ExpenseUpdate(
            title=new_title,
            amount=new_amount,
            category=new_category,
            payment_method=new_payment_method,
            notes=new_notes,
        )

        return expense_service.edit_expense(
            title=title,
            category=category,
            amount=amount,
            payment_method=payment_method,
            expense_date=(
                datetime.fromisoformat(expense_date)
                if expense_date
                else None
            ),
            updates=updates,
        )