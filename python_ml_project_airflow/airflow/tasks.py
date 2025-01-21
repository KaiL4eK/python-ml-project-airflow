"""Module for tasks definition.

Define only taskflow (decorator) tasks here.
    Main logic has to be independent from Airflow.
In API Service ~ Application to interact with user so it contains main logic.
    In comparison Routes in API define only when to call Services.
So in Airflow we define Tasks and Services.
    Tasks just define Airflow dependent things, Services define logic.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from time import sleep

from airflow.decorators import task
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from pendulum import DateTime  # noqa: TC002

from python_ml_project_airflow.services import show_logic_time, simple_logic

logger = logging.getLogger(__name__)


@task
def simple_task_taskflow() -> None:
    """Sample task for taskflow."""
    return simple_logic()


# Another way to define task
simple_task_operator = PythonOperator(
    task_id="simple_task_operator",
    python_callable=simple_logic,
)


@task
def show_logic_time_task(logical_date: DateTime) -> None:
    """Task to debug logical time."""
    logical_ts = datetime.fromtimestamp(logical_date.timestamp(), tz=timezone.utc)
    return show_logic_time(logical_ts=logical_ts)


@task
def sample_sleep_task(sleep_time: int) -> None:
    """Task just to capture worker."""
    sleep(sleep_time)


@task
def show_sample_variable() -> None:
    """Sample task to access Variables."""
    sample_variable = Variable.get("SAMPLE_VARIABLE")
    logger.info(f"SAMPLE_VARIABLE={sample_variable}")
