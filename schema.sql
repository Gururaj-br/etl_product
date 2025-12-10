DROP DATABASE IF EXISTS etl_test;
CREATE DATABASE etl_test;
USE etl_test;

CREATE TABLE customer (
  customer_id INT PRIMARY KEY,
  age INT
);

CREATE TABLE items (
  item_id INT PRIMARY KEY,
  item_name VARCHAR(100)
);

CREATE TABLE sales (
  sales_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  sales_id INT,
  item_id INT,
  quantity INT,
  FOREIGN KEY (sales_id) REFERENCES sales(sales_id),
  FOREIGN KEY (item_id) REFERENCES items(item_id)
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