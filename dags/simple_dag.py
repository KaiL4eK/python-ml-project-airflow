"""Sample DAG."""

from datetime import datetime

from airflow.decorators import dag

from python_ml_project_airflow.airflow.tasks import (
    show_logic_time_task,
    simple_task_operator,
    simple_task_taskflow,
)


@dag(
    dag_id="simple-dag",
    start_date=datetime(2025, 1, 1),  # noqa: DTZ001
    schedule_interval=None,
    catchup=False,
)
def simple_dag() -> None:
    """Sample DAG."""
    simple_task_taskflow() >> simple_task_operator >> show_logic_time_task()


simple_dag()
