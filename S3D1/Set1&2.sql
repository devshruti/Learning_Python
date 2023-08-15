-- **Problem 1:**
-- - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
-- - **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.

CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(15)
);


-- **Problem 2:**
-- - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
-- - **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (1, 'John Doe', 'john@example.com', '123 Main St', '555-1234'),
    (2, 'Jane Smith', 'jane@example.com', '456 Oak Ave', '555-5678'),
    (3, 'Alice Johnson', 'alice@example.com', '789 Elm Rd', '555-9876'),
    (4, 'Bob Williams', 'bob@example.com', '321 Pine Ln', '555-4321'),
    (5, 'Eve Brown', 'eve@example.com', '654 Maple Ct', '555-8765');



-- **Problem 3:**
-- - **Prerequisite**: Understand basic data fetching in SQL / MongoDB
-- - **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

SELECT * FROM Customers;


-- **Problem 4:**
-- - **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
-- - **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

SELECT name, email FROM Customers;


-- **Problem 5:**
-- - **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
-- - **Problem**: Write a query to fetch the customer with the **`id`** of 3.

SELECT * FROM Customers WHERE id = 3;


-- **Problem 6:**
-- - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.

SELECT * FROM Customers WHERE name LIKE 'A%';


-- **Problem 7:**
-- - **Prerequisite**: Understand how to order data in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.

SELECT * FROM Customers ORDER BY name DESC;


-- **Problem 8:**
-- - **Prerequisite**: Understand data updating in SQL / MongoDB
-- - **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.

UPDATE Customers SET address = '987 Cedar Rd' WHERE id = 4;


-- **Problem 9:**
-- - **Prerequisite**: Understand how to limit results in SQL / MongoDB
-- - **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

SELECT * FROM Customers ORDER BY id ASC LIMIT 3;


-- **Problem 10:**
-- - **Prerequisite**: Understand data deletion in SQL / MongoDB
-- - **Problem**: Write a query to delete the customer with **`id`** 2.

DELETE FROM Customers WHERE id = 2;


-- **Problem 11:**
-- - **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to count the number of customers.

SELECT COUNT(*) FROM Customers;


-- **Problem 12:**
-- - **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.

SELECT * FROM Customers ORDER BY id ASC OFFSET 2;


-- **Problem 13:**
-- - **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.
SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';


-- **Problem 14:**
-- - **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.
SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';


-- **Problem 15:**
-- - **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.
SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';


-- **Problem 16:*
-- - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
-- - **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    cuisine_type VARCHAR(255),
    delivery_available BOOLEAN,
    average_rating DECIMAL(3, 2)
);


-- **Problem 17:**
-- - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
-- - **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.
INSERT INTO Restaurants (id, name, location, cuisine_type, delivery_available, average_rating)
VALUES
    (1, 'Restaurant A', 'New York', 'Italian', true, 4.5),
    (2, 'Restaurant B', 'Los Angeles', 'Mexican', false, 3.8),
    (3, 'Restaurant C', 'Chicago', 'Steakhouse', true, 4.2),
    (4, 'Restaurant D', 'Miami', 'Seafood', true, 4.7),
    (5, 'Restaurant E', 'San Francisco', 'Japanese', false, 4.0);


-- **Problem 18:**
-- - **Prerequisite**: Understand how to order data in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.
SELECT * FROM Restaurants ORDER BY average_rating DESC;


-- **Problem 19:**
-- - **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.
SELECT * FROM Restaurants WHERE delivery_available = true AND average_rating > 4;


-- **Problem 20:**
-- - **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.
SELECT * FROM Restaurants WHERE cuisine_type IS NULL OR cuisine_type = '';


-- **Problem 21:**
-- - **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.
SELECT COUNT(*) FROM Restaurants WHERE delivery_available = true;


-- **Problem 22:**
-- - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
-- - **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.
SELECT * FROM Restaurants WHERE location LIKE '%New York%';


-- **Problem 23:**
-- - **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
-- - **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.
SELECT AVG(average_rating) FROM Restaurants;


-- **Problem 24:**
-- - **Prerequisite**: Understand how to limit results in SQL / MongoDB
-- - **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.
SELECT * FROM Restaurants ORDER BY average_rating DESC LIMIT 5;


-- **Problem 25:**
-- - **Prerequisite**: Understand data deletion in SQL / MongoDB
-- - **Problem**: Write a query to delete the restaurant w
DELETE FROM Restaurants WHERE id = 3;
