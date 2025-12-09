
DROP DATABASE IF EXISTS etl_test;
CREATE DATABASE etl_test;
USE etl_test;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT
);

CREATE TABLE order_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT,
  quantity INT
);

CREATE TABLE pipeline_run (
  job_token VARCHAR(64),
  process_name VARCHAR(100),
  step_name VARCHAR(50),
  status VARCHAR(20),
  start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  end_time TIMESTAMP NULL,
  PRIMARY KEY (job_token, step_name)
);
