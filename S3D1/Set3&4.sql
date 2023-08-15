-- **Problem 26:**
-- - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
-- - **Problem**: Create a **`Rides`** table / collection with the fields defined above.
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5, 2),
    fare DECIMAL(7, 2),
    ride_time INT
);


-- **Problem 27:**
-- - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
-- - **Problem**: Insert five rows / documents into the **`Rides`** table / collection with data of your choice.
INSERT INTO Rides (id, driver_id, start_location, end_location, distance, fare, ride_time)
VALUES
    (1, 101, 'Suburb A', 'Downtown', 10.5, 25.50, 20),
    (2, 102, 'Suburb B', 'Airport', 18.2, 42.75, 30),
    (3, 103, 'Suburb C', 'Downtown', 7.8, 18.25, 15),
    (4, 104, 'Suburb D', 'Shopping Mall', 5.0, 12.00, 10),
    (5, 105, 'Suburb E', 'Downtown', 12.7, 30.00, 25);


-- **Problem 28:**
-- - **Prerequisite**: Understand how to order data in SQL / MongoDB
-- - **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.
SELECT * FROM Rides ORDER BY fare DESC;


-- **Problem 29:**
-- - **Prerequisite**: Understand using math operations in SQL / MongoDB
-- - **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.
SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare FROM Rides;


-- **Problem 30:**
-- - **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
-- - **Problem**: Write a query to calculate the average **`ride_time`** of all rides.
SELECT AVG(ride_time) FROM Rides;


-- **Problem 31:**
-- - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
-- - **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.
SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';


-- **Problem 32:**
-- - **Prerequisite**: Understand how to use the COUNT function in SQL / MongoDB's aggregate functions
-- - **Problem**: Write a query to count the number of rides for a given **`driver_id`**.
SELECT COUNT(*) FROM Rides WHERE driver_id = 103;


-- **Problem 33:**
-- - **Prerequisite**: Understand data updating in SQL / MongoDB
-- - **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.
UPDATE Rides SET fare = 15.50 WHERE id = 4;


-- **Problem 34:**
-- - **Prerequisite**: Understand using GROUP BY in SQL / MongoDB's aggregate functions
-- - **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.
SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;


-- **Problem 35:**
-- - **Prerequisite**: Understand data deletion in SQL / MongoDB
-- - **Problem**: Write a query to delete the ride with **`id`** 2.
DELETE FROM Rides WHERE id = 2;


-- **Problem 36:**
-- - **Prerequisite**: Understand using the MAX and MIN functions in SQL / using sort and limit in MongoDB
-- - **Problem**: Write a query to find the ride with the highest and lowest **`fare`**.
-- Highest fare
SELECT * FROM Rides ORDER BY fare DESC LIMIT 1;

-- Lowest fare
SELECT * FROM Rides ORDER BY fare ASC LIMIT 1;


-- **Problem 37:**
-- - **Prerequisite**: Understand using the GROUP BY clause in SQL / using aggregate in MongoDB
-- - **Problem**: Write a query to find the average **`fare`** and **`distance`** for each **`driver_id`**.
SELECT driver_id, AVG(fare) AS avg_fare, AVG(distance) AS avg_distance
FROM Rides
GROUP BY driver_id;


-- **Problem 38:**
-- - **Prerequisite**: Understand using HAVING clause in SQL / using match in MongoDB's aggregate pipeline
-- - **Problem**: Write a query to find **`driver_id`** that have completed more than 5 rides.
SELECT driver_id, COUNT(*) AS ride_count
FROM Rides
GROUP BY driver_id
HAVING ride_count > 5;


-- **Problem 39:**
-- - **Prerequisite**: Understand the use of INNER JOIN in SQL / Lookup in MongoDB
-- - **Problem**: Assuming there is another collection/table called **`Drivers`** with **`driver_id`** and **`name`** fields, write a query to find the name of the driver with the highest **`fare`**.
SELECT Drivers.name
FROM Rides
JOIN Drivers ON Rides.driver_id = Drivers.driver_id
ORDER BY fare DESC
LIMIT 1;


-- **Problem 40:**
-- - **Prerequisite**: Understand the concept of subqueries in SQL / using multiple stages in MongoDB's aggregate pipeline
-- - **Problem**: Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.
SELECT driver_id, SUM(fare) AS total_earnings
FROM Rides
GROUP BY driver_id
ORDER BY total_earnings DESC
LIMIT 3;


-- **Problem 41:**
-- - **Prerequisite**: Understand date and time functions in SQL / MongoDB
-- - **Problem**: Assuming there's a **`ride_date`** field of date type in the **`Rides`** table / collection, write a query to find all rides that happened in the last 7 days.
SELECT * FROM Rides
WHERE ride_date >= DATE_SUB(NOW(), INTERVAL 7 DAY);


-- **Problem 42:**
-- - **Prerequisite**: Understand the concept of NULL values and how to handle them in SQL / MongoDB
-- - **Problem**: Write a query to find all rides where the **`end_location`** is not set.
SELECT * FROM Rides WHERE end_location IS NULL;


-- **Problem 43:**
-- - **Prerequisite**: Understand the use of complex mathematical operations in SQL / MongoDB
-- - **Problem**: Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.
SELECT id, fare / distance AS fare_per_mile
FROM Rides
ORDER BY fare_per_mile DESC;


-- **Problem 44:**
-- - **Prerequisite**: Understand the use of multiple JOINs in SQL / multiple Lookups in MongoDB
-- - **Problem**: Assuming there's another collection/table **`Passengers`** with **`passenger_id`** and **`name`** fields, write a query to return a list of all rides including the driver's name and passenger's name.
SELECT Rides.*, Drivers.name AS driver_name, Passengers.name AS passenger_name
FROM Rides
JOIN Drivers ON Rides.driver_id = Drivers.driver_id
JOIN Passengers ON Rides.passenger_id = Passengers.passenger_id;


-- **Problem 45:**
-- - **Prerequisite**: Understand how to alter table schemas in SQL / adding and modifying fields in MongoDB documents
-- - **Problem**: Write a query to add a
ALTER TABLE Rides
ADD COLUMN ride_type VARCHAR(255);


