# Airflow - Boilerplate
![CI](https://github.com/N0-man/airflow-dbt-boilerplate/actions/workflows/ci.yml/badge.svg)

This repo contains example Airflow DAGs with various unit tests to show how you can implement automated testing of your DAGs.

DAG validation tests are written using `pytest`

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