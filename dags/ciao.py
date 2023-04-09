import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def greet():
    print('Writing in file')
    with open('greet.txt', 'a+', encoding='utf8') as f:
        print(f.read())
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'


def respond():
    return 'Greet Responded Again'


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2023, 1, 1, 10, 00, 00),
    'concurrency': 1,
    'retries': 2
}

with DAG('io_resto_casa',
         catchup=False,
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         # schedule_interval=None,
         ) as dag:
    opr_hello = BashOperator(task_id='say_Hi',
                             bash_command='echo "Doing Hi in Italian!!"')

    opr_greet = PythonOperator(task_id='greet',
                               python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep_me',
                             bash_command='sleep 5')

    opr_respond = PythonOperator(task_id='respond',
                                 python_callable=respond)

opr_hello >> opr_greet >> opr_sleep >> opr_respond