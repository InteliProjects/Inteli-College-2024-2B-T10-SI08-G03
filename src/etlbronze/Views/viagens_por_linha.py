from clickhouse_connect import get_client
from services.create_view import NewView

class ViagensPorLinha:
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
            toDate(JSONExtractFloat(data_linha, 'DT_INI_VIAGEM')) AS travel_date,
            JSONExtractString(data_linha, 'TX_DESCR_LINHA') AS line,
            COUNT(*) AS total_travels

            FROM grupo3.working_travels

            WHERE data_tag = 'big-data-viagem_viagem_tabela_principal'
            
            GROUP BY 
                travel_date,
                line
            ORDER BY 
                travel_date ASC,
                line ASC;
        """
        new_view.create_view(
            view_name="viagens_por_linha",
            query=query
        )