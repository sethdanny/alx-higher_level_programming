-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user and grant privileges
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_1'@'localhost';
