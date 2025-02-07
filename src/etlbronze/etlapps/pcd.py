from prefect import task
from services.servicesetl.serviceextract.extract import Extract
from services.servicesetl.servicetransform.transformpcd import Transform
from services.servicesetl.serviceloading.loading import Loading

class PcdPipeline:
    def __init__(self):
        pass

    @task
    def main(self):
        # Chamando os métodos em sequência
        data_path, data_tag, name_table = self.extract()
        transformed_data = self.transform(data_path, name_table)
        self.load(transformed_data, data_tag, name_table)

    @task
    def extract(self):
        # Extração dos dados
        extract = Extract()
        data_path, data_tag, name_table = extract.save_data('big-data-PCD/acompanhamento_pcd.parquet')
        return data_path, data_tag, name_table

    @task
    def transform(self, data_path, name_table):
        # Transformação dos dados
        transform = Transform(data_path, name_table)
        transformed_data = transform.transform_data()
        return transformed_data

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
