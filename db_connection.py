import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes;"
    f"Encrypt=no;"
)

# test it
df = pd.read_sql("SELECT TOP 5 * FROM Sales.SalesOrderHeader", connection)
print(df)