from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default settings applied to all tasks
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    'hendi_b2b_pipeline',
    default_args=default_args,
    description='Automated daily ELT Pipeline for HENDI',
    schedule_interval='@daily', # Runs automatically once a day
    catchup=False,
) as dag:

    # Task 1: Execute the extraction script
    extract_task = BashOperator(
        task_id='extract_mock_data',
        bash_command='cd /opt/airflow/dags && python extract_mock_data.py',
    )

    # Task 2: Execute the loading script
    load_task = BashOperator(
        task_id='load_to_snowflake',
        bash_command='cd /opt/airflow/dags && python load_to_snowflake.py',
    )

    # Define the dependency (Task 1 must finish before Task 2 starts)
    extract_task >> load_task
