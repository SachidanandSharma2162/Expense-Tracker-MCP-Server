from app.database.connection import mongodb

db = mongodb.get_database()

print("✅ Connected Successfully!")
print("Database:", db.name)