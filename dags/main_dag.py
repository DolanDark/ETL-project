try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    #import pandas as pd

    print("All Dag modules are working")
except Exception as e:
    print("Error  {} ".format(e))


def data_collect():
    import json_builder
    os.system('python json_builder.py')
    print("Hello world")
    return "Json Built!"

def database_load():
    import neo4j_query
    os.system('python neo4j_query')
    print("Hello again")
    return "Loaded to database!"
    

with DAG(
        dag_id="main_dag",
        schedule_interval="@daily",     #cron expression can be added accordingly
        default_args={
            "owner": "akash",
            "retries": 1,
            "retry_daily": timedelta(minutes=5),
            "start_date" : datetime(2021, 5, 10),   #the start date is set to a month before so that it executes for the past 30 days when run
        },
        catchup=False) as f:

    data_collect = PythonOperator(
        task_id="data_collect",
        python_callable=data_collect

    )

    database_load = PythonOperator(
        task_id="database_load",
        python_callable=database_load,
        provide_context=True
    )

data_collect >> database_load       #flow of execution