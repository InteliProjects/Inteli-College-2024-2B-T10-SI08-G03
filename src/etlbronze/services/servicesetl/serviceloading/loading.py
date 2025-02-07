from clickhouse_connect import get_client
import pandas as pd
import time
import datetime
from services.obs_conn import log_observability

class Loading:
    def __init__(self, clickhouse_host: str, clickhouse_database: str, username: str = None, password: str = None):
        self.client = get_client(
            host=clickhouse_host,
            port=8123,
            database=clickhouse_database,
            username=username,
            password=password
        )

    def load_data(self, data: list, data_tag: str, name_table: str):
        print("Starting data loading...")
        start_time = datetime.datetime.utcnow()
        data_ingestao = int(time.time())
        
        formatted_data = [
            {
                "data_ingestao": data_ingestao,
                "data_linha": row,
                "data_tag": data_tag
            }
            for row in data
        ]

        df = pd.DataFrame(formatted_data)
        expected_columns = ['data_ingestao', 'data_linha', 'data_tag']
        df = df[expected_columns]
        df.reset_index(drop=True, inplace=True)
        df['data_ingestao'] = df['data_ingestao'].astype(int)
        df['data_linha'] = df['data_linha'].astype(str)
        df['data_tag'] = df['data_tag'].astype(str)

        try:
            self.client.insert("working_travels", df, column_names=expected_columns)
            end_time = datetime.datetime.utcnow()
            details = {
                "status": "success",
                "records_loaded": len(df),
                "data_tag": data_tag,
                "table_name": name_table
            }
            log_observability("Loading", start_time, end_time, details, name_table)
            print(f"Successfully loaded {len(df)} records into {name_table} with tag {data_tag}.")
        except Exception as e:
            end_time = datetime.datetime.utcnow()
            details = {
                "status": "error",
                "error_message": str(e),
                "records_attempted": len(df)
            }
            log_observability("Loading", start_time, end_time, details, name_table)
            print(f"Error loading data into ClickHouse: {e}")