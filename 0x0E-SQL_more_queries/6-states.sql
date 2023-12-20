-- Will create the DB hbtn_0d_usa and the table.

-- creates a DB if not existed.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to the DB
USE hbtn_0d_usa;

-- creates a table if not existed
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
