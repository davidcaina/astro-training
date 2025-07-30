from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def run_lambda_function():
    with open('/tmp/dummy', 'rb') as f:
        print(f.read().decode('utf-8'))

with DAG(
    dag_id='check_dag',
    start_date=datetime(2023, 1, 1),
    description='DAG responsible to check something daily',
    schedule='@daily',
    tags=['data_engineer'],
    catchup=False
) as dag:

    create_file = BashOperator(
        task_id="create_file",
        bash_command='echo "Hi there!" > /tmp/dummy'
    )

    check_file = BashOperator(
        task_id="check_file",
        bash_command='test -f /tmp/dummy'
    )

    read_file = PythonOperator(
        task_id="read_file",
        python_callable=run_lambda_function
    )

    create_file >> check_file >> read_file
