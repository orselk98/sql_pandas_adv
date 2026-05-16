import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import connection
import pandas as pd

df = pd.read_sql("""
           SELECT Name,
                  FirstName,
                  LastName,
                  TotalSpending
From (
SELECT  st.Name,
        p.FirstName,
        p.LastName,
        sum(soh.TotalDue) as TotalSpending,
        ROW_NUMBER () Over (
            PARTITION BY st.NAME
            ORDER BY sum(soh.TotalDue) desc
        ) as RowNum
from sales.SalesTerritory as st 
join Sales.SalesOrderHeader as soh on st.TerritoryID = soh.TerritoryID
join sales.Customer as c on soh.CustomerID = c.CustomerID
join Person.Person as p on c.PersonID = p.BusinessEntityID
group by st.Name,p.FirstName,p.LastName
) as ranked
where RowNum <= 10
""", connection)

print (df)