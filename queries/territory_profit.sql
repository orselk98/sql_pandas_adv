use AdventureWorks
go

SELECT st.Name,
        AVG(LineTotal -(StandardCost* OrderQty))/AVG(LineTotal) *100 as ProfitPercentage,
        SUM(linetotal) as TotalSales
from sales.SalesTerritory as st  
JOIN sales.SalesOrderHeader as soh ON st.TerritoryID = soh.TerritoryID
JOIN sales.SalesOrderDetail as sod on sod.SalesOrderID = soh.SalesOrderID
join Production.Product as p on p.ProductID = sod.ProductID
GROUP by st.Name
ORDER by ProfitPercentage desc