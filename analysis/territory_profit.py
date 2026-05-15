import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import plotly.express as px

from db_connection import connection
import pandas as pd
import plotly

df = pd.read_sql("""
SELECT st.Name,
        AVG(LineTotal -(StandardCost* OrderQty))/AVG(LineTotal) *100 as ProfitPercentage,
        SUM(linetotal) as TotalSales
from sales.SalesTerritory as st  
JOIN sales.SalesOrderHeader as soh ON st.TerritoryID = soh.TerritoryID
JOIN sales.SalesOrderDetail as sod on sod.SalesOrderID = soh.SalesOrderID
join Production.Product as p on p.ProductID = sod.ProductID
GROUP by st.Name
ORDER by ProfitPercentage desc
""", connection)

#create the bar chart

fig = px.bar(df, x='Name', y='ProfitPercentage', title='Profit Percentage by Sales Territory')
fig.show()
fig.write_html("dashboard/territory_profit.html")