from clickhouse_connect import get_client
import pandas as pd
import time

class Loading:
    def __init__(self, clickhouse_host: str, clickhouse_database: str, username: str = None, password: str = None):
        self.client = get_client(
            host=clickhouse_host,
            port=8123,
            database=clickhouse_database,
            username=username,
            password=password
        )

    def load_data(self, data: list, data_tag: str):
        print("Starting data loading...")
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
            print(f"Inserting {len(df)} records into ClickHouse...")
            self.client.insert('working_travels', df, column_names=expected_columns)
            print(f"Loaded {len(df)} records to ClickHouse.")
        except Exception as e:
            print(f"Error loading data into ClickHouse: {e}")


data = pd.read_csv('dmo_anl_vw_estacao (1).csv')

#converter cada linha para a estrutura [{coluna 1: dado 1}, {coluna 2: dado 2}]
data = data.to_dict(orient='records')

#instanciar a classe Loading
load = Loading(
    clickhouse_host="srv613520.hstgr.cloud",
    clickhouse_database="grupo3",
    username="admin",
    password="admin123"
)
load.load_data(data, "big-data-estacoes/estacoes.parquet")

