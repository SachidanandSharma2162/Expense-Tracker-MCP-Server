from fastmcp import FastMCP

from app.tools.add_expense import register_add_expense_tool
from app.tools.list_expense import register_list_expense_tool
from app.tools.edit_expense import register_edit_expense_tool
from app.tools.delete_expense import register_delete_expense_tool
from app.tools.summarize import register_summary_tool

mcp = FastMCP("Expense Tracker",)

register_add_expense_tool(mcp)
register_list_expense_tool(mcp)
register_edit_expense_tool(mcp)
register_delete_expense_tool(mcp)
register_summary_tool(mcp)
if __name__ == "__main__":
    mcp.run()