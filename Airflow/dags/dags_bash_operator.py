from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator.py",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2006, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2
    
        