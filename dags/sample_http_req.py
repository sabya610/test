### Importing Python Modules


from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Retry after 5 minutes if a task fails
}

# Define the DAG (Directed Acyclic Graph)
dag = DAG(
    'simple_dag_example',
    default_args=default_args,
    description='A simple DAG with two tasks',
    schedule_interval= '*/10 * * * *',  # Runs every 10 minutes per day
    start_date=days_ago(2),  # Start date is 2 days ago
    catchup=False,  # Do not backfill if start date is in the past
    access_control={
		'All': {
			'can_read',
			'can_edit',
			'can_delete'
		}
	}
)

# Task 1: Print the current date using BashOperator
print_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task 2: Sleep for 5 seconds using BashOperator
sleep_task = BashOperator(
    task_id='sleep_task',
    bash_command='sleep 5',
    dag=dag,
)

# Define task dependencies
# sleep_task will run after print_date
print_date >> sleep_task

