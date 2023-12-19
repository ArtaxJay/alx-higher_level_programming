-- Will create hbtn_0d_2 DB and user_0d_2

-- cmd creates a DB if not existed
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- cmd creates a user if not existed
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- cmd allows SELECT query privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
