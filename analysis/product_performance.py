import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import connection
import pandas as pd

df = pd.read_sql("""
select pc.Name, 
       YEAR(soh.OrderDate) as orderyear,
       sum(LineTotal) as totalrevenue,
       sum(StandardCost * sod.OrderQty) as totalcost
from Production.Product pp
JOIN Production.ProductSubCategory psc on pp.ProductSubcategoryID = psc.ProductSubcategoryID
join Production.ProductCategory pc on psc.ProductCategoryID = pc.ProductCategoryID
join sales.SalesOrderDetail sod on pp.ProductID = sod.ProductID
join sales.SalesOrderHeader soh on sod.SalesOrderID = soh.SalesOrderID
GROUP BY pc.Name, YEAR(soh.OrderDate)
""", connection)

print (df)