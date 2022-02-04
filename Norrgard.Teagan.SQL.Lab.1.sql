# 1.	Write a query to get Product name and quantity/unit
Select northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;

# 2. Write a query to get current Product list (Product ID and name).  
Select northwind.products.id, northwind.products.product_name FROM northwind.products;

# 3. Write a query to get discontinued Product list (Product ID and name). 
Select northwind.products.product_name, northwind.products.id FROM northwind.products 
WHERE northwind.products.discontinued='1';

# 4. Write a query to get most expense and least expensive Product list (name and unit price).  
Select northwind.products.list_price, northwind.products.product_name FROM northwind.products
WHERE list_price = (Select MAX(list_price) from northwind.products) OR 
list_price = (Select MIN(list_price) from northwind.products);

# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.  
Select northwind.products.id, northwind.products.product_name, northwind.products.list_price 
FROM northwind.products WHERE list_price <= 20;

# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
Select northwind.products.list_price, northwind.products.id, northwind.products.product_name 
FROM northwind.products WHERE list_price >= 15 AND list_price <= 25;

# 7. Write a query to get Product list (name, unit price) of above average price.  
Select northwind.products.list_price, northwind.products.product_name FROM northwind.products 
WHERE list_price > standard_cost;

# 8. Write a query to get Product list (name, unit price) of ten most expensive products.  
Select northwind.products.list_price, northwind.products.product_name FROM northwind.products 
ORDER BY list_price DESC LIMIT 10;

# 9. Write a query to count current and discontinued products. 
SELECT northwind.products.discontinued,COUNT(*) FROM northwind.products GROUP BY discontinued;

# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
Select northwind.products.product_name, northwind.products.quantity_per_unit, 
northwind.products.minimum_reorder_quantity FROM northwind.products 
WHERE quantity_per_unit < minimum_reorder_quantity;

