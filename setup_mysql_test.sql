-- This script creates a database for AirBnB clone project for testing

-- Creates a "hbnb_test_db" database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a new user called "hbnb_test" on the localhost
-- With password "hbnb_test_pwd"
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db for the new user
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database performance_schema for the new user
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
