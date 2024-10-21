from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import polars as pl

# Function to process data with pandas
def process_with_pandas():
        # Read CSV using pandas
            df = pd.read_csv('/path/to/your/input_file.csv')
                # Example processing: calculate mean of a column
                    mean_value = df['your_column'].mean()
                        print(f'Mean value (Pandas): {mean_value}')
                            # Save processed data
                                df.to_csv('/path/to/your/pandas_output.csv', index=False)

                                # Function to process data with polars
                                def process_with_polars():
                                        # Read CSV using polars
                                            df = pl.read_csv('/path/to/your/input_file.csv')
                                                # Example processing: calculate mean of a column
                                                    mean_value = df['your_column'].mean()
                                                        print(f'Mean value (Polars): {mean_value}')
                                                            # Save processed data
                                                                df.write_csv('/path/to/your/polars_output.csv')

                                                                # Define the DAG
                                                                with DAG(
                                                                            'simple_data_processing_dag',
                                                                                default_args={
                                                                                            'owner': 'airflow',
                                                                                                    'start_date': datetime(2024, 11, 1),
                                                                                                            'retries': 1,
                                                                                                                },
                                                                                    schedule_interval='@daily',  # Adjust the schedule as needed
                                                                                    ) as dag:
                                                                        
                                                                        task_pandas = PythonOperator(
                                                                                        task_id='process_with_pandas',
                                                                                                python_callable=process_with_pandas,
                                                                                                    )

                                                                            task_polars = PythonOperator(
                                                                                            task_id='process_with_polars',
                                                                                                    python_callable=process_with_polars,
                                                                                                        )
                                                                            access_control={
                                                                                            'All': {
                                                                                                            'can_read',
                                                                                                                        'can_edit',
                                                                                                                                    'can_delete'
                                                                                                                                            }
                                                                                                }
                                                                            )

                                                                                # Define task dependencies
                                                                                    task_pandas >> task_polars
