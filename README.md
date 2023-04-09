# Airflow - Boilerplate

This repo contains example Airflow DAGs with a DAG validation test suite to show how you can implement automated testing of your DAGs.

DAG validation tests are written using `pytest`

### Prerequisite
* [Docker](https://docs.docker.com/get-docker/) 
* [Docker Compose](https://docs.docker.com/compose/install/)
* [python](https://www.python.org/downloads/) 
* [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)


## Run
Start Airflow stack. The webserver should be available on `http://0.0.0.0:8080/home` 
```
docker compose up
```

## Install
```
pip install -r requirements.txt
```
## Test
```
pytest --tb=short --disable-pytest-warnings --verbose
```