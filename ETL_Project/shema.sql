drop database dataSet_db;

-- Create and use dataSet1
create database dataSet_db;
USE dataSet_db;

-- Create tables for raw data to be loaded into
CREATE TABLE dataSet1 (
id INT,
first_name TEXT,
last_name TEXT,
gender TEXT
PRIMARY KEY(id)
);

CREATE TABLE dataSet2 (
id INT,
user_id INT,
marital_s TEXT,
occupation TEXT,
annual_income FLOAT,
PRIMARY KEY(id)
FOREIGN KEY (user_id)
        REFERENCES dataSet1(id)
        ON DELETE CASCADE
);
