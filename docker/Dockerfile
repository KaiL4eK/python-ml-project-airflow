# Custom Airflow image to install dependencies
ARG AIRFLOW_IMAGE_NAME=apache/airflow:2.10.4
FROM ${AIRFLOW_IMAGE_NAME}

# `root` user to install everything
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
  && pip install -r requirements.project.txt

COPY docker/scripts/ ./scripts/
