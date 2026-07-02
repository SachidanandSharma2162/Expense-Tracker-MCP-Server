from typing import Optional

from fastmcp import FastMCP

from app.models.expense import Category
from app.services.expense_service import expense_service


def register_list_expense_tool(mcp: FastMCP):
    """
    Register the list_expenses MCP tool.
    """

    @mcp.tool
    def list_expenses(
        category: Optional[Category] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """
        List down all the expenses based on the category.
        Use this tool whenever the user wants to see the list of expenses,,
        payment, bill, or any money spent.
        """

        expenses = expense_service.list_expenses(
            category=category,
            limit=limit,
        )

        return {
            "success": True,
            "count": len(expenses),
            "expenses": expenses,
        }