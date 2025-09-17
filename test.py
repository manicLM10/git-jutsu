

# Define a simple Python function for the PythonOperator
def process_data():
    print("Processing data...")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Instantiate the DAG
with DAG(
    dag_id='sample_practice_dag',
    default_args=default_args,
    description='A simple practice DAG',
    schedule_interval='@daily',  # Runs daily
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Define tasks
    start = DummyOperator(
        task_id='start',
    )

    process = PythonOperator(
        task_id='process',
        python_callable=process_data,
    )

    end = DummyOperator(
        task_id='end',
    )

    # Set task dependencies
    start >> process >> end
#hari change in edit UI 
#hari change in edit UI 2
