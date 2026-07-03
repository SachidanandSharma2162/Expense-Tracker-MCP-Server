from fastmcp import FastMCP

from app.services.expense_service import expense_service


def register_summary_tool(mcp: FastMCP):

    @mcp.tool
    def summarize_expenses():
        """
        Return analytics and statistics about expenses.
        """
        return expense_service.get_overall_summary()