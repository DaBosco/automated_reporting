import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="changeme",
    database="reports_db"
)

print("✅ MariaDB connected")

conn.close()
