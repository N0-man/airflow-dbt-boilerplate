import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def greet():
    print('Writing in file')
    msg = 'Greeted: '
    with open('greet.txt', 'a+', encoding='utf8') as f:
        msg += f.read()
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return msg


def greet_again():
    return 'Greet Responded Again'


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2023, 4, 7, 10, 00, 00),
    'concurrency': 1,
    'retries': 2
}

with DAG('io_resto_casa',
         catchup=False,
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         # schedule_interval=None,
         ) as dag:
    opr_init = BashOperator(task_id='init',
                             bash_command='echo "Doing Hi in Italian!!"')

    opr_greet = PythonOperator(task_id='greet',
                               python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep',
                             bash_command='sleep 5')

    opr_greet_again = PythonOperator(task_id='greet_again',
                                 python_callable=greet_again)

opr_init >> opr_greet >> opr_sleep >> opr_greet_again