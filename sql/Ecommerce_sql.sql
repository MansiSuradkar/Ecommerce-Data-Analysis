/* Calculate Total Revenue*/
SELECT ROUND(SUM(Quantity * UnitPrice),2) AS Total_Revenue 
FROM online_retail_cleaned;

/*Find Top-Selling Products*/
SELECT
    StockCode,
    Description,
    SUM(Quantity) AS Total_Quantity
FROM online_retail_cleaned
GROUP BY StockCode, Description
ORDER BY Total_Quantity DESC
LIMIT 10;

/*Find Top 10 Customers*/
SELECT
    CustomerID,
    ROUND(SUM(Quantity * UnitPrice),2) AS Total_Spending
FROM online_retail_cleaned
GROUP BY CustomerID
ORDER BY Total_Spending DESC
LIMIT 10;

/*Calculate Average Order Value*/
SELECT
    ROUND(AVG(Order_Value),2) AS Average_Order_Value
FROM
(
    SELECT
        InvoiceNo,
        SUM(Quantity * UnitPrice) AS Order_Value
    FROM online_retail_cleaned
    GROUP BY InvoiceNo
) AS Orders;

/*Monthly Sales Analysis*/
SELECT
    DATE_FORMAT(InvoiceDate,'%Y-%m') AS Month,
    ROUND(SUM(Quantity * UnitPrice),2) AS Revenue
FROM online_retail_cleaned
GROUP BY Month
ORDER BY Month;

/*Find Repeat Customers*/
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM online_retail_cleaned
GROUP BY CustomerID
HAVING COUNT(DISTINCT InvoiceNo) > 1
ORDER BY Total_Orders DESC
LIMIT 10;

/*Category-wise Sales*/
SELECT
    Description,
    ROUND(SUM(Quantity * UnitPrice),2) AS Revenue
FROM online_retail_cleaned
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 100;

/*Product Ranking*/
SELECT
    StockCode,
    Description,
    ROUND(SUM(Quantity * UnitPrice),2) AS Revenue,
    RANK() OVER (
        ORDER BY SUM(Quantity * UnitPrice) DESC
    ) AS Product_Rank
FROM online_retail_cleaned
GROUP BY StockCode, Description;

/*Customer Order Frequency*/
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Order_Frequency
FROM online_retail_cleaned
GROUP BY CustomerID
ORDER BY Order_Frequency DESC
LIMIT 100;

/*Revenue by Country*/
SELECT
    Country,
    ROUND(SUM(Quantity * UnitPrice),2) AS Revenue
FROM online_retail_cleaned
GROUP BY Country
ORDER BY Revenue DESC;

