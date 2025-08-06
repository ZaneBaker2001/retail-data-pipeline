# Retail Real-Time Analytics Pipeline

## Overview
A full-stack data pipeline for real-time transaction monitoring using Kafka, Spark, Pandas, PostgreSQL, and Airflow.

## Project Structure
- `ingestion/`: Kafka producer to simulate transactions
- `streaming/`: Spark job to process and store raw data
- `batch/`: Daily ETL jobs to load into data warehouse
- `airflow/`: DAG to schedule batch jobs
- `warehouse/`: PostgreSQL schema
- `docker/`: contains both of the necessary files to setup Docker
- `data/`: contains two empty files that will be populated with data whenever the project is run

## Requirements
```bash
pip install -r requirements.txt
```

## Cloud Integration
- Store raw parquet files in AWS S3 instead of local disk (use `boto3`)
- Load data into Amazon RDS PostgreSQL or Redshift

## Dockerization (Optional)
Add Docker Compose setup for Kafka, Spark, PostgreSQL, and Airflow.
