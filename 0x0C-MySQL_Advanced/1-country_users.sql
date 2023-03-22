-- 1. In and not out
-- create a table user (attribute enum)
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255), 
    country ENUM('US', 'CO', 'TN')NOT NULL);
