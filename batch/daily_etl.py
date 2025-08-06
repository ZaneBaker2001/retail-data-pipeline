import pandas as pd
from sqlalchemy import create_engine
import logging

def run_etl():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting ETL job...")

    df = pd.read_parquet('data/raw')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    engine = create_engine('postgresql://user:password@localhost:5432/retail_dw')
    df.to_sql('fact_transactions', engine, if_exists='append', index=False)

    logging.info("ETL job completed.")
