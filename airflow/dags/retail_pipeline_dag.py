from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from batch.daily_etl import run_etl

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

dag = DAG('retail_pipeline', default_args=default_args, schedule_interval='@daily')

etl_task = PythonOperator(
    task_id='run_daily_etl',
    python_callable=run_etl,
    dag=dag
)

etl_task
