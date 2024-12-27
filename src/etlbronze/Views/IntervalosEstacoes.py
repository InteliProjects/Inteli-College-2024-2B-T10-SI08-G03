from services.create_view import NewView

class IntervalosEstacoes: 
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
        WITH
            data_completa AS (
                SELECT
                    JSONExtractString(data_linha, 'Open_Time') AS raw_open_time,
                    trimBoth(JSONExtractString(data_linha, 'Open_Time')) AS open_time,
                    JSONExtractInt(data_linha, 'Station_ID') AS station_id,
                    -- Substituir toDate por parseDateTimeBestEffort
                    parseDateTimeBestEffort(substring(trimBoth(JSONExtractString(data_linha, 'Open_Time')), 1, 10)) AS dia
                FROM
                    grupo5.data_ingestion di
                WHERE
                    JSONExtractString(data_linha, 'Open_Time') != '' -- Ignorar strings vazias
            ),
            data_ordenada AS (
                SELECT
                    dia,
                    station_id,
                    arraySort(groupArray(open_time)) AS horarios
                FROM
                    data_completa
                GROUP BY
                    dia, station_id
            ),
            intervalos AS (
                SELECT
                    dia,
                    station_id,
                    arrayDifference(arrayMap(x -> toUnixTimestamp(parseDateTimeBestEffort(x)), horarios)) / 60 AS intervalos_minutos
                FROM
                    data_ordenada
            )
        SELECT
            dia,
            station_id,
            AVG(arrayJoin(intervalos_minutos)) AS media_intervalo
        FROM
            intervalos
        GROUP BY
            dia, station_id
        ORDER BY
            dia, station_id;
        """

        new_view.create_view("station_line_day_intervals", query)

        