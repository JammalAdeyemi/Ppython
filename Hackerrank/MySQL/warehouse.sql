-- 1. SQL: Warehouse Accounting System Customer Report
-- As part of the development of a warehouse accounting system, create a report that lists customers' companies and the total number of active warehouses they have. Additional information about active warehouses is also required, such as the volume of the smallest warehouse, the volume of the largest warehouse, and the total volume of all warehouses.

-- The result should have the following columns: name | warehouses | min_volume | max_volume | total_volume
-- name - customer name
-- warehouses - the total number of active warehouses for a specific customer
-- min_volume - the volume of the smallest active warehouse for a specific customer
-- max_volume - the volume of the largest active warehouse for a specific customer
-- total_volume - the total volume of all active warehouse for a specific customer

-- The result should be sorted in ascending order by name.

-- -- Note: Only active warehouses should be included in the report.

SELECT 
    c.name AS name,
    COUNT(w.customer_id) AS warehouses,
    MIN(w.volume) AS min_volume,
    MAX(w.volume) AS max_volume,
    SUM(w.volume) AS total_volume
FROM 
    customers c
JOIN 
    warehouses w 
ON 
    c.id = w.customer_id
WHERE 
    w.is_active = 1
GROUP BY 
    c.name
ORDER BY 
    c.name ASC
;