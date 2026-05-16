import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import connection
import pandas as pd

df = pd.read_sql("""
SELECT p.FirstName,p.LastName,sp.BusinessEntityID, sum(soh.TotalDue) as TotalSales
FROM sales.SalesOrderHeader as soh
join sales.SalesPerson as sp on soh.SalesPersonID = sp.BusinessEntityID
JOIN HumanResources.Employee as e on sp.BusinessEntityID = e.BusinessEntityID
join Person.Person as p on e.BusinessEntityID=p.BusinessEntityID
GROUP BY p.FirstName,p.LastName,sp.BusinessEntityID
ORDER BY TotalSales DESC
""", connection)

print (df)