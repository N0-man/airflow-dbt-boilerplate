import pytest
from airflow.models import DagBag

@pytest.fixture()
def dagbag():
    return DagBag(dag_folder='dags/', include_examples=False)
def get_task(dag, id):
    for task in dag.tasks:
        if task.task_id == id:
            return task
    
def test_no_import_errors():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  assert len(dag_bag.import_errors) == 0, "No Import Failures"


def test_retries_present():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  for dag in dag_bag.dags:
      retries = dag_bag.dags[dag].default_args.get('retries', [])
      error_msg = 'Retries not set to 2 for DAG {id}'.format(id=dag)
      assert retries == 2, error_msg

def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4
    

def test_init_task(dagbag):
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    init_task = get_task(dag, "init")
    assert init_task.task_type == 'BashOperator'
    assert len(init_task.upstream_task_ids) == 0  #First Task
    assert len(init_task.downstream_task_ids) == 1
    assert sorted(init_task.downstream_task_ids) == sorted({'greet'})
        
def test_greet_task(dagbag):
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    greet_task = get_task(dag, "greet")
    assert greet_task.task_type == 'PythonOperator'
    assert len(greet_task.upstream_task_ids) == 1
    assert sorted(greet_task.upstream_task_ids) == sorted({'init'}) # Only triggered by init
    assert len(greet_task.downstream_task_ids) == 1
    assert sorted(greet_task.downstream_task_ids) == sorted({'sleep'})
    
def test_sleep_task(dagbag):
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    sleep_task = get_task(dag, "sleep")
    assert sleep_task.task_type == 'BashOperator'
    assert len(sleep_task.upstream_task_ids) == 1
    assert sorted(sleep_task.upstream_task_ids) == sorted({'greet'}) # Only triggered by greet
    assert len(sleep_task.downstream_task_ids) == 1
    assert sorted(sleep_task.downstream_task_ids) == sorted({'greet_again'})

def test_greet_again_task(dagbag):
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    greet_again_task = get_task(dag, "greet_again")
    assert greet_again_task.task_type == 'PythonOperator'
    assert len(greet_again_task.upstream_task_ids) == 1
    assert sorted(greet_again_task.upstream_task_ids) == sorted({'sleep'}) # Only triggered by sleep
    assert len(greet_again_task.downstream_task_ids) == 0 # Last  task