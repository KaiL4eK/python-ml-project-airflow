import json
import os

from airflow import settings
from airflow.models import Connection


def add_connection(conn_id: str, conn_cfg: str):
    """
    conn_cfg — либо строка-URI (postgres://…),
                либо JSON со свойствами Connection:
      {
        "conn_type": "...",
        "description": "...",
        "login": "...",
        "password": "...",
        "host": "...",
        "port": "...",
        "schema": "...",
        "extra": "..."
      }
    """
    session = settings.Session()
    existing = session.query(Connection).filter(Connection.conn_id == conn_id).first()
    if existing:
        print(f"Connection '{conn_id}' already exists, skipping creation.")
        session.close()
        return

    print(f"Adding connection: {conn_id}: {conn_cfg}")

    conn: Connection = None
    try:
        cfg = json.loads(conn_cfg)
        if isinstance(cfg, dict):
            conn = Connection(
                conn_id=conn_id,
                **cfg,
            )
    except json.JSONDecodeError:
        # Если не создалось из JSON — трактуем как URI
        conn = Connection(conn_id=conn_id, uri=conn_cfg)

    session.add(conn)
    session.commit()
    print(f"Connection {conn_id} added.")


def main():
    raw = os.getenv("SAMPLE_POSTGRES_CONNECTION")
    if not raw:
        raise RuntimeError("Environment variable SAMPLE_POSTGRES_CONNECTION is not set")
    add_connection("sample_postgres_connection", raw)


if __name__ == "__main__":
    main()
