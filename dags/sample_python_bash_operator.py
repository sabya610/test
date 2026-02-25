from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param


# Python function for PythonOperator
def greet_user(**context):
    name = "Airflow User"
    print(f"Hello {name}, Airflow DAG is working!")


default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "retries": 1,
}


with DAG(
    dag_id="example_python_bash_email_dag",
    default_args=default_args,
    schedule_interval=None,
    tags=["ezaf"],
    params={
        "airgap_registry_url": Param(
            "",
            type=["null", "string"],
            pattern=r"^$|^\S+/$",
            description="Airgap registry url. Trailing slash in the end is required",
        ),
        "email": Param("airflow@example.com", type="string",description="Enter EMail ID"),
    },
    render_template_as_native_obj=True,
    access_control={"All": {"can_read", "can_edit", "can_delete"}},
) as dag:

    # Task 1: Python operator
    python_task = PythonOperator(
        task_id="python_task",
        python_callable=greet_user,
    )

    # Task 2: Bash operator
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo 'Running Bash Task from Airflow!'",
    )


    # Task dependencies
    python_task >> bash_task 
