-- create database if doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table within the database
CREATE TABLE IF NOT EXISTS states
(id INT NOT NULL AUTO INCREMENT,
name VARCHAR(256) NOT NULL, UNIQUE(id));
