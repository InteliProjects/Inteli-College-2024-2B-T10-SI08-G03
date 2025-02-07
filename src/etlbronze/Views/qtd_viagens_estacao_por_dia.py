from services.create_view import NewView

class ViagensEstacaoDia:
    def _init_(self):
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
    toDate(JSONExtractFloat(data_linha, 'dt_origin')) AS travel_date,
    JSONExtractString(data_linha, 'TX_ORIGEM_PROG') AS station,
    COUNT(*) AS total_travels
    FROM grupo3.working_travels
    GROUP BY
    travel_date,
    station
    ORDER BY
    travel_date ASC,
    station ASC;
        """

        new_view.create_view("viagens_estacao_dia", query)
