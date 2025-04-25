#!/usr/bin/env bash

# mkdir -p /sources/logs /sources/dags /sources/plugins
chown -R "${AIRFLOW_UID}:0" /opt/airflow/{logs,dags,plugins}

# Install package to system in dev mode
# pip install -e .

# Must be last as exec replaces current shell and completes
exec /entrypoint airflow version
