#!/usr/bin/env bash

# mkdir -p /sources/logs /sources/dags /sources/plugins
chown -R "${AIRFLOW_UID}:0" /opt/airflow/{logs,dags,plugins}
exec /entrypoint airflow version

# Install package to system in dev mode
pip install -e .

# NOTE: during init you can insert variables to Airflow and define other resources
