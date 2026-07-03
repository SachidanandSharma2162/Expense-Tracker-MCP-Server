# 💰 Expense Tracker MCP Server

A personal AI-powered Expense Tracker built using **FastMCP**, **MongoDB**, and **Claude Desktop**.

This project demonstrates how to build a production-style **Model Context Protocol (MCP)** server with a clean layered architecture. Instead of interacting with a traditional UI, users can manage their expenses using natural language through Claude Desktop.

---

## ✨ Features

- ➕ Add Expenses
- 📋 List Expenses
- ✏️ Edit Expenses using natural language
- 🗑️ Delete Expenses without remembering IDs
- 📊 Expense Summary & Analytics
- 🏷️ Automatic Category Management
- 💳 Multiple Payment Methods
- 🔢 Auto-generated Expense IDs (EXP0001, EXP0002...)
- 🗄️ MongoDB Persistence
- 🤖 Claude Desktop Integration
- ⚡ FastMCP Server

---

# 🏗️ Project Architecture

```
                Claude Desktop
                      │
                      ▼
              FastMCP Server
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Add Expense      Edit Expense     Delete Expense
      │               │                │
      └───────────────┼────────────────┘
                      ▼
              Expense Service
                      │
                      ▼
          Expense Repository
                      │
                      ▼
                 MongoDB Atlas
```

The project follows a layered architecture:

- **Tools Layer** → MCP Tool definitions
- **Service Layer** → Business Logic
- **Repository Layer** → Database Operations
- **Database Layer** → MongoDB

This keeps the project clean, scalable, and easy to maintain.

---

# 📁 Project Structure

```
expense-tracker-mcp/
│
├── app/
│   ├── config.py
│
│   ├── database/
│   │   ├── connection.py
│   │   ├── counters.py
│   │   └── expense_repository.py
│
│   ├── models/
│   │   └── expense.py
│
│   ├── services/
│   │   └── expense_service.py
│
│   ├── tools/
│   │   ├── add_expense.py
│   │   ├── list_expenses.py
│   │   ├── edit_expense.py
│   │   ├── delete_expense.py
│   │   ├── summarize.py
│
├── .env
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Tech Stack

- Python 3.12+
- FastMCP
- MongoDB Atlas
- PyMongo
- Pydantic
- Claude Desktop
- dotenv

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/expense-tracker-mcp.git

cd expense-tracker-mcp
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file

```env
MONGODB_URI=your_mongodb_connection_string

DATABASE_NAME=expense_tracker

COLLECTION_NAME=expenses

COUNTER_COLLECTION=counters
```

---

## Run the MCP Server

```bash
python main.py
```

or

```bash
fastmcp run main.py
```

---

# Claude Desktop Configuration

Example configuration:

```json
{
  "mcpServers": {
    "expense-tracker": {
      "command": "fastmcp",
      "args": [
        "run",
        "C:\\Users\\YourName\\Desktop\\expense-tracker-mcp\\main.py"
      ]
    }
  }
}
```

Restart Claude Desktop after updating the configuration.

---

# 📌 Available MCP Tools

## ➕ Add Expense

Example prompts:

> Add ₹250 for Lunch using UPI

> I spent ₹1200 on Shopping using Credit Card

---

## 📋 List Expenses

Examples:

> Show all expenses

> Show my last 5 expenses

> Show Food expenses

---

## ✏️ Edit Expense

No need to remember Expense IDs.

Examples:

> Change my Lunch expense to ₹350

> Update Coffee payment method to Card

> Move Uber expense to Travel category

---

## 🗑️ Delete Expense

Examples:

> Delete my Lunch expense

> Delete today's Coffee expense

---

## 📊 Summary

Examples:

> Summarize my expenses

Returns

- Total Spending
- Number of Expenses
- Average Expense
- Highest Expense
- Lowest Expense

---

# Example Conversation

### User

```
Add ₹250 for Lunch using UPI
```

Claude

```
✅ Expense Added Successfully

Expense ID : EXP0007
Title      : Lunch
Amount     : ₹250
Category   : Food
Payment    : UPI
```

---

### User

```
Change my Lunch expense to ₹300
```

Claude

```
✅ Expense Updated Successfully
```

---

### User

```
Summarize my expenses
```

Claude

```
Total Spending : ₹8450

Expenses       : 22

Average        : ₹384

Highest        : ₹1200

Lowest         : ₹50
```

---

# MongoDB Collections

### Expenses

```json
{
  "expense_id": "EXP0001",
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "payment_method": "UPI",
  "notes": "",
  "date": "2026-07-03T12:30:00",
  "created_at": "...",
  "updated_at": "..."
}
```

---

### Counters

```json
{
  "_id": "expense_id",
  "sequence_value": 42
}
```

---

# Learning Outcomes

This project helped me understand:

- Model Context Protocol (MCP)
- FastMCP Development
- Claude Desktop Integration
- MongoDB CRUD Operations
- MongoDB Aggregation Pipelines
- Repository Pattern
- Service Layer Architecture
- Pydantic Models
- Environment Configuration
- AI Tool Design
- Natural Language Tool Invocation

---

# Future Enhancements

- 📅 Monthly Analytics
- 📈 Category-wise Spending
- 💰 Budget Management
- 📤 CSV / Excel Export
- 🔁 Recurring Expenses
- 📊 Spending Trends
- 🤖 AI Spending Insights
- 🌐 Web Dashboard

---

# Author

**Sachidanand Sharma**

M.Tech CSE @ IIIT Lucknow

- 🤖 AI & MCP Enthusiast
- ☁️ Learning DevOps
- 💻 Competitive Programmer

---

# License

This project is licensed under the MIT License.

Feel free to fork, improve, and build upon it.

---

⭐ If you found this project useful, consider giving it a star!