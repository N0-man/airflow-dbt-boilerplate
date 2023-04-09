# Airflow - Boilerplate
![CI](https://github.com/N0-man/airflow-dbt-boilerplate/actions/workflows/ci.yml/badge.svg)

This repo contains 
* Example Airflow DAGs. Unit tests coverage includes
    - Verify import errors
    - Veriry dag config such as retry count
    - Verify if the dag is loaded with requried tasks
    - Verify each task, its operator and its upstream and downstream dependencies are as expected
* Example custom operator with unit test
    - Verify response from custom operator

### Prerequisite
* [Docker](https://docs.docker.com/get-docker/) 
* [Docker Compose](https://docs.docker.com/compose/install/)
* [python](https://www.python.org/downloads/) 
* [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

## Install
```
pip install -r requirements.txt
```
## Initialise Airflow db
```
airflow db init
```
## Test
```
pytest --tb=short --disable-pytest-warnings --verbose
```
## Docker Setup
You can also setup Airflow stack using docker compose. The webserver should be available on `http://0.0.0.0:8080/home` 
```
docker compose up
```