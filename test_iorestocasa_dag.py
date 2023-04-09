# import pytest
# from airflow.models import DagBag

# @pytest.fixture()
# def dagbag():
#     return DagBag(dag_folder='dags/', include_examples=False)

# def test_no_import_errors():
#   dag_bag = DagBag(dag_folder='dags/', include_examples=False)
#   assert len(dag_bag.import_errors) == 0, "No Import Failures"


# def test_retries_present():
#   dag_bag = DagBag(dag_folder='dags/', include_examples=False)
#   for dag in dag_bag.dags:
#       retries = dag_bag.dags[dag].default_args.get('retries', [])
#       error_msg = 'Retries not set to 2 for DAG {id}'.format(id=dag)
#       assert retries == 1, error_msg

# def test_dag_loaded(dagbag):
#     dag = dagbag.get_dag(dag_id="io_resto_casa")
#     assert dagbag.import_errors == {}
#     assert dag is not None
#     assert len(dag.tasks) == 3

import pytest

from airflow.models import DagBag

@pytest.fixture()
def dagbag():
    return DagBag(dag_folder='dags/', include_examples=False)
    
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
    print(dagbag)
    dag = dagbag.get_dag(dag_id="io_resto_casa")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4