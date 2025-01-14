from airflow import DAG

from airflow.operators.python import PythonOperator

from pendulum import datetime

import mlflow

import logging

import os

import base64

 

#Try to add token like below and then rest of the flow. Also check for any indentation if broken while copying it here. 
 
######################################
 
def interact_with_mlflow():
    with open("/etc/secrets/ezua/.auth_token", "r") as f:
        auth_token = f.read().strip()  # Ensure to strip any whitespace
 
    AWS_ENDPOINT_URL = "http://local-s3-service.ezdata-system.svc.cluster.local:30000"  
    MLFLOW_S3_ENDPOINT_URL = AWS_ENDPOINT_URL
    os.environ["MLFLOW_S3_IGNORE_TLS"] = "true"
    os.environ["MLFLOW_TRACKING_INSECURE_TLS"] = "true"
    os.environ["MLFLOW_TRACKING_TOKEN"] = auth_token
    os.environ["AUTH_TOKEN"] = auth_token
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = MLFLOW_S3_ENDPOINT_URL
    os.environ["AWS_ENDPOINT_URL"] = AWS_ENDPOINT_URL
    os.environ["AWS_ACCESS_KEY_ID"] = auth_token  # Ensure correct AWS access key
    os.environ["AWS_SECRET_ACCESS_KEY"] = "s3"  # Ensure correct secret key
    mlflow.set_tracking_uri("http://mlflow.mlflow.svc.cluster.local:5000")

 

 

def search_mlflow_runs():

    experiment_name = "test_tszamel"

    experiment = mlflow.get_experiment_by_name(experiment_name)

 

    if experiment:

        runs = mlflow.search_runs(filter_string="tags.mlflow.runName = 'prophet'")

        logging.info(runs)

    else:

        raise ValueError(f"Experiment {experiment_name} not found.")

 

 

default_args = {

    "owner": "airflow",

    "depends_on_past": False,

    "start_date": datetime(2024, 9, 19, 9, 30),

    "email_on_failure": False,

    "email_on_retry": False,

}

 

with DAG(

    "mlflow_airflow_connection_test",

    default_args=default_args,

    description="DAG to search MLflow experiment runs",

    schedule_interval=None,

    tags=["mlflow"],

    catchup=False,

    access_control={

        "Admin": {"can_edit", "can_read", "can_delete"},

    },

) as dag:

    search_runs_task = PythonOperator(

        task_id="search_mlflow_runs",

        python_callable=search_mlflow_runs,

    )

  

    search_runs_task
