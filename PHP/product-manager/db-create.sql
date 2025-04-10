CREATE DATABASE IF NOT EXISTS product_db;

USE product_db;

CREATE TABLE IF NOT EXISTS list (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    url TEXT NOT NULL
);
