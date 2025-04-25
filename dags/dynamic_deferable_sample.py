from datetime import datetime

from airflow.decorators import dag, task, task_group
from airflow.models.param import Param
from airflow.operators.python import get_current_context
from airflow.providers.postgres.hooks.postgres import PostgresHook

from python_ml_project_airflow.airflow.sensors.async_pg_sql_sensor import (
    DeferrableAsyncSqlSensor,
)


@dag(
    dag_id="dynamic_deferrable_sql_sensor",
    start_date=datetime(2025, 4, 1),
    schedule_interval=None,
    catchup=False,
    params={
        "num_groups": Param(1, type="integer", minimum=1),
    },
    tags=["example", "postgres"],
)
def dynamic_sensor_dag():
    @task
    def generate_indices() -> list[int]:
        ctx = get_current_context()
        num = ctx["params"]["num_groups"]
        return list(range(num))

    @task
    def sleep_task():
        import time
        time.sleep(1)

    @task
    def insert_result(idx: int):
        hook = PostgresHook(postgres_conn_id="sample_postgres_connection")
        hook.run(
            sql=(
                "INSERT INTO result_table (task_index, execution_time) "
                "VALUES (%s, NOW())"
            ),
            parameters=(idx,),
        )

    @task_group
    def process_group(idx: int):
        sleeper = sleep_task()
        sensor = DeferrableAsyncSqlSensor(
            task_id="wait_for_row",
            conn_id="sample_postgres_connection",
            sql="SELECT id FROM wait_table WHERE data = 'sample data';",
            poke_interval=15,
            timeout=300,
        )
        inserter = insert_result(idx)
        sleeper >> sensor >> inserter

    indices = generate_indices()
    process_group.expand(idx=indices)

dag = dynamic_sensor_dag()
