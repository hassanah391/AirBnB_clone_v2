-- This script creates a database for AirBnB clone project

-- Creates a "hbnb_dev_db" database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a new user called "hbnb_dev" in the localhost
-- With password "hbnb_dev_pwd"
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db for the new user
GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the database performance_schema for the new user
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
