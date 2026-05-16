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