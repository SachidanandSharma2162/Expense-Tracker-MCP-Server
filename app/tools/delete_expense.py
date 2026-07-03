from datetime import datetime
from typing import Optional

from fastmcp import FastMCP

from app.models.expense import (
    Category,
    PaymentMethod,
)
from app.services.expense_service import expense_service


def register_delete_expense_tool(mcp: FastMCP):
    """
    Register the delete_expense MCP tool.
    """

    @mcp.tool
    def delete_expense(
        title: Optional[str] = None,
        category: Optional[Category] = None,
        amount: Optional[float] = None,
        payment_method: Optional[PaymentMethod] = None,
        expense_date: Optional[str] = None,
    ) -> dict:
        """
        Delete an expense by searching for it.
        You do not need to know the expense ID."""
        return expense_service.delete_expense(
            title=title,
            category=category,
            amount=amount,
            payment_method=payment_method,
            expense_date=(
                datetime.fromisoformat(expense_date)
                if expense_date
                else None
            ),
        )