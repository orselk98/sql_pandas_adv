use AdventureWorks
GO

SELECT *
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
