CREATE TABLE fact_transactions (
    transaction_id VARCHAR PRIMARY KEY,
    timestamp TIMESTAMP,
    date DATE,
    store_id INT,
    product_id INT,
    amount DECIMAL
);

CREATE TABLE dim_store (
    store_id INT PRIMARY KEY,
    store_name VARCHAR,
    region VARCHAR
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR
);

CREATE INDEX idx_store_date ON fact_transactions (store_id, date);
