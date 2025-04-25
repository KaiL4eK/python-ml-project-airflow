# Custom Airflow image to install dependencies
ARG AIRFLOW_IMAGE_NAME=apache/airflow:2.10.4-python3.9
FROM ${AIRFLOW_IMAGE_NAME}

# `root` user to install everything
# vim - just as an example, remove if apt not required
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Back to `airflow` user
USER airflow

# README.md is required for installation later (during init)
COPY requirements.project.txt pyproject.toml poetry.lock README.md ./
RUN pip install --upgrade pip \
  && pip install -r requirements.project.txt \
  && poetry export --only main --format=requirements.txt > requirements.txt \
  && pip install -r requirements.txt

COPY docker/scripts/ ./scripts/

COPY python_ml_project_airflow ./python_ml_project_airflow/
RUN pip install .
