import smtplib
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Retry after 5 minutes if a task fails
}

dag=DAG(
     'simple_mail',
     default_args=default_args,
     description='Simple task to send mail',
     schedule_interval=None,
     start_date=days_ago(2),
     catchup=False

)



def hpe_email():
 
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
 
    SUBJECT = "SMTP e-mail test"
    TEXT = f"Hello , How are you doing {date_time}"
 
    message = f'Subject: {SUBJECT}\n\n{TEXT}'
 
    print(f"%%%%%%%%% MESSAGE = {message} %%%%%%%%")
 
    sender = 'sabyasachi.mallik@hpe.com'
    receivers = 'sabyasachi.mallik@hpe.com'
 
    try:
        smtpObj = smtplib.SMTP('smtp.its.hpecorp.net')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
 
    except smtplib.SMTPException:
        print("Error: unable to send email")
 
    # Close the connection
    smtpObj.close()

#Task 1 :Print current date using Bash Operator
print_date=BashOperator(
     task_id='Print_Date',
     bash_command='date',
     dag=dag
)

#Task 2: Send Mail using smtp and pythonoperator
mail_send=PythonOperator(
      task_id='Mail_Sending_Task',
      python_callable=hpe_email,
      dag=dag
)

print_date>>mail_send
