# How to run code locally for debug

- [Local Airflow run](#local-airflow-run)
  - [Run standalone session](#run-standalone-session)
- [Local Airflow run using Docker](#local-airflow-run-using-docker)
- [Specific functions run locally](#specific-functions-run-locally)


## Local Airflow run

> Don`t forget that Airflow re-reads DAGs periodically, so you can update your code and it will run updated without need to restart Airflow itself.

### Run standalone session

Just call next comman and it will run standalone local Airflow.

```bash
make airflow-standalone-run
```

During start console will show `admin` password. It will be permanent until you remove `airflow-home` directory.

You can find Airflow on `http://localhost:8080/`.

> Airflow configuration is done in [airflow-home/airflow.cfg](../airflow-home/airflow.cfg) (main config) and [.env.airflow.standalone](../.env.airflow.standalone) (override).

## Local Airflow run using Docker

TODO =)

## Specific functions run locally

> For examples check [notebooks](../notebooks/airflow-dev/local_functions_run.ipynb)
