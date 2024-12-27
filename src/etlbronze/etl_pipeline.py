from prefect import flow, task
from dotenv import load_dotenv
from etlapps.pcd import PcdPipeline
from etlapps.intervalos import IntervalosPipeline
from etlapps.viagens import ViagensPipeline
from Views.viagens_por_linha import ViagensPorLinha
from Views.qtd_viagens_estacao_por_dia import ViagensEstacaoDia
from Views.qtd_pcd_dia import QtdPcdDia
from Views.intervalo_de_trens import IntervalosTrensEstacoes
from Views.IntervalosEstacoes import IntervalosEstacoes
from Views.qtd_viagens_dia import QtdViagensDia
from Views.media_parado_por_estacao import MediaEstacoes

load_dotenv()

class EtlPipeline:

    @task
    def extract(self, pipeline, name_table):
        data = pipeline.extract(name_table)
        if len(data) != 3:
            raise ValueError(f"Expected extract to return 3 values, got {len(data)}")
        print(f"Extracted data from {name_table}: {data}")
        return data

    @task
    def transform(self, pipeline, data_path, name_table):
        transformed_data = pipeline.transform(data_path, name_table)
        print(f"Transformed data for {name_table}")
        return transformed_data

    @task
    def load(self, pipeline, transformed_data, data_tag, name_table):
        pipeline.load(transformed_data, data_tag, name_table)
        print(f"Loaded data into the database for {name_table}")
        return True

    @task
    def run_intervalos(self):
        name_table = "DMO-ANL"
        print(f"Starting ETL for table: {name_table}")
        pipeline = IntervalosPipeline()  
        pipeline.main()  
        return True

    @task
    def run_pcd(self):
        name_table = "PCD"
        print(f"Starting ETL for table: {name_table}")
        pipeline = PcdPipeline() 
        pipeline.main() 
        return True

    def run_viagens(self):
        name_table = "viagem"
        print(f"Starting ETL for table: {name_table}")
        pipeline = ViagensPipeline()  
        pipeline.main()
        return True 

    @task
    def create_qtd_viagens_estacao_por_dia(self):
        view = ViagensEstacaoDia()
        view.create_view()
        pipeline = ViagensPipeline()
        pipeline.main()
        return True
        
    @task
    def create_intervalos_trens_estações(self):
        view = IntervalosTrensEstacoes()
        view.create_view()
        return True

    @task
    def create_media_intervalo_por_dia_estacao(self):
        view = IntervalosEstacoes()
        view.create_view()
        return True

    @task
    def create_qtd_pcd_dia(self):
        view = QtdPcdDia()
        view.create_view()
        return True
        
    @task
    def create_qtd_viagens_dia(self):
        view = QtdViagensDia()
        view.create_view()
        return True
    
    @task
    def create_media_tempo_pausa_estacoes(self):
        view = MediaEstacoes()
        view.create_view()
        return True

    @task
    def create_viagens_por_linha(self):
        view = ViagensPorLinha()
        view.create_view()

    @flow(log_prints=True)
    def run_all(self):
        print("Starting ETL for all tables")
        self.run_intervalos()
        self.run_pcd()
        self.run_viagens()
        self.create_viagens_por_linha()
        self.create_qtd_viagens_estacao_por_dia()
        self.create_qtd_pcd_dia()
        self.create_intervalos_trens_estações()
        self.create_media_intervalo_por_dia_estacao()
        self.create_qtd_viagens_dia()
        self.create_media_tempo_pausa_estacoes()
        print("ETL for all tables completed")
        return True

if __name__ == "__main__":
    pipeline = EtlPipeline()
    print("Executing ETL Pipeline")
    pipeline.run_all()