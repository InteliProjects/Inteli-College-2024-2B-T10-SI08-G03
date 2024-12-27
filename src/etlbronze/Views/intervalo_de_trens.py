from services.create_view import NewView

class IntervalosTrensEstacoes:
    def __init__(self):
        pass
    
    def create_view(self):
        new_view = NewView(
            clickhouse_host="srv613520.hstgr.cloud",
            clickhouse_database="grupo3",
            username="admin",
            password="admin123"
        )
        
        query ="""
            WITH
                FilteredData AS (
                    SELECT
                        JSONExtractInt(data_linha, 'Station_ID') AS Curr_Station,
                        JSONExtractInt(data_linha, 'NextStation_ID') AS Next_Station,
                        JSONExtractInt(data_linha, 'Line_ID') AS Line_ID,
                        JSONExtractInt(data_linha, 'Train_ID') AS Train_ID,
                        parseDateTimeBestEffort(JSONExtractString(data_linha, 'Closed_Time')) AS Closed_Time,
                        parseDateTimeBestEffort(JSONExtractString(data_linha, 'Open_Time')) AS Open_Time
                    FROM grupo5.data_ingestion
                    WHERE data_tag = 'caixapreta/trem_passageiros.parquet'
                    AND JSONHas(data_linha, 'Station_ID') 
                    AND JSONHas(data_linha, 'NextStation_ID') 
                    AND JSONHas(data_linha, 'Closed_Time')
                    AND JSONHas(data_linha, 'Open_Time')
                ),
                -- Numerando as estações para relacioná-las por viagens consecutivas
                NumberedStations AS (
                    SELECT
                        *,
                        ROW_NUMBER() OVER (PARTITION BY Line_ID, Train_ID ORDER BY Closed_Time) AS Row_Num
                    FROM FilteredData
                ),
                -- Mapeamento dos nomes das estações
                StationInfo AS (
                    SELECT
                        JSONExtractInt(replaceAll(data_linha, '''', '"'), 'id_estacao') AS Station_ID,
                        JSONExtractString(replaceAll(data_linha, '''', '"'), 'tx_nome') AS Station_Name
                    FROM grupo3.working_travels wt 
                    WHERE data_tag = 'big-data-estacoes/estacoes.parquet'
                )
            SELECT
                t1.Curr_Station,
                s1.Station_Name AS Curr_Station_Name,
                t1.Next_Station,
                s2.Station_Name AS Next_Station_Name,
                AVG(dateDiff('second', t1.Closed_Time, t2.Open_Time)) / 60 AS Avg_Travel_Time_Minutes
            FROM
                NumberedStations t1
            INNER JOIN
                NumberedStations t2
                ON t1.Row_Num + 1 = t2.Row_Num
                AND t1.Line_ID = t2.Line_ID
                AND t1.Train_ID = t2.Train_ID
            LEFT JOIN
                StationInfo s1
                ON t1.Curr_Station = s1.Station_ID
            LEFT JOIN
                StationInfo s2
                ON t1.Next_Station = s2.Station_ID
            GROUP BY
                t1.Curr_Station,
                s1.Station_Name,
                t1.Next_Station,
                s2.Station_Name
            ORDER BY
                t1.Curr_Station,
                t1.Next_Station;
        """
        
        new_view.create_view("intervalos_estacoes_trens", query)
        
        