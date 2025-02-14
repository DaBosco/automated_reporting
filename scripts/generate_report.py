from sqlalchemy import create_engine
import pandas as pd

DB_USER = "root"
DB_PASSWORD = "changeme"
DB_HOST = "localhost"
DB_NAME = "reports_db"

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

query = "SELECT * FROM sales_report;"

df = pd.read_sql(query, engine)

csv_path = "/automated_reporting/data/sales_report.csv"
df.to_csv(csv_path, index=False)

print(f"✅ Report generated successfully! Saved in {csv_path}")

