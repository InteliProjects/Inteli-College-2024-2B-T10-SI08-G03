from services.create_view import NewView

class MediaEstacoes:
    def __init__(self) -> None:
        pass

    def create_view(self):
        new_view = NewView(
            clickhouse_host="srv613520.hstgr.cloud",
            clickhouse_database="grupo3",
            username="admin",
            password="admin123"
        )

        query = """
            SELECT
                JSONExtractString(data_linha, 'Station_ID') AS station,
                AVG(
                    toUnixTimestamp(parseDateTimeBestEffort(JSONExtractString(data_linha, 'Closed_Time'))) -
                    toUnixTimestamp(parseDateTimeBestEffort(JSONExtractString(data_linha, 'Open_Time')))
                ) AS avg_train_stop_seconds
            FROM 
                grupo5.data_ingestion
            WHERE 
                "data_tag" = 'caixapreta/trem_passageiros.parquet'
            GROUP BY
                station;
        """

        new_view.create_view("media_tempo_pausa_estacoes", query)