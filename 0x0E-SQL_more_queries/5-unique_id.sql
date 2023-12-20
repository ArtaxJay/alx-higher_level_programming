-- Will create a table called unique_id on MySQL server

-- cmd creates a table if not existed
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
