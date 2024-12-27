from services.create_view import NewView

class QtdPcdDia:
    def __init__(self):
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
                JSONExtractInt(data_linha, 'alert_station_id') AS station_id,
                COUNT(*) AS total_pcd
            FROM grupo3.working_travels
            WHERE
                JSONExtractString(data_linha, 'pcd_type') != ''
            GROUP BY
                travel_date,
                station_id
            ORDER BY
                travel_date ASC,
                station_id ASC;
                """
        new_view.create_view("qtd_pcd_dia", query)