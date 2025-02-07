from prefect import task
from services.servicesetl.serviceextract.extract import Extract
from services.servicesetl.servicetransform.transformintervalos import Transform
from services.servicesetl.serviceloading.loading import Loading

class IntervalosPipeline:
    def __init__(self):
        pass

    @task
    def main(self):
        # Chamando os métodos sequencialmente
        data_path, data_tag, name_table = self.extract()
        intervalo = self.transform(data_path, name_table)
        self.load(intervalo, data_tag, name_table)

    @task
    def extract(self):
        # Extraindo dados
        extract = Extract()
        data_path, data_tag, name_table = extract.save_data('big-data-DMO-ANL/intervalos.parquet')
        return data_path, data_tag, name_table

    @task
    def transform(self, data_path, name_table):
        # Transformando dados
        transform = Transform(data_path, name_table)
        intervalo = transform.transform_data()
        return intervalo

    @task
    def load(self, transformed_data, data_tag, name_table):
        # Carregando dados para o banco
        load = Loading(
            clickhouse_host="srv613520.hstgr.cloud",
            clickhouse_database="grupo3",
            username="admin",
            password="admin123"
        )
        load.load_data(transformed_data, data_tag, name_table)
