import datetime
import json 
from .connections import get_postgres_connection

async def log_observability(metric_name, start_time, end_time, details, name_table):
    conn = get_postgres_connection()
    cursor = conn.cursor()
    
    start_time_unix = int(start_time.timestamp())
    end_time_unix = int(end_time.timestamp())
    duration = datetime.timedelta(seconds=(end_time_unix - start_time_unix))

    await cursor.execute('''
        CREATE TABLE IF NOT EXISTS modulo8si.observability_g3 (
            id SERIAL PRIMARY KEY,
            metric_name VARCHAR(255),
            start_time BIGINT,
            end_time BIGINT,
            duration INTERVAL,
            details JSON,
            name_table VARCHAR(255)
        )
    ''')

    details = json.dumps(details) if isinstance(details, dict) else details

    cursor.execute('''
        INSERT INTO modulo8si.observability_g3 (metric_name, start_time, end_time, duration, details, name_table)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (metric_name, start_time_unix, end_time_unix, duration, details, name_table))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Logged {metric_name} metrics successfully.")
