
# Airflow Imports:
from airflow import DAG
from airflow.operators.python import PythonOperator

# Others imports:
from datetime import datetime

def print_a():
    print('Hellow World')

def print_b():
    print('Hellow World 2')

with DAG(
        'my_dag',
        start_date=datetime(2023, 1, 1),
        description='A simple tutorial DAG',
        schedule='@daily',
        tags=['data_science'],
        catchup=False) as dag:
    
    task_a = PythonOperator( task_id='task_a', python_callable=print_a)

    task_b = PythonOperator( task_id='task_b', python_callable=print_b)

    task_a >> task_b