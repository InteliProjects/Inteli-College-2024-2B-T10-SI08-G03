import pandas as pd
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ConfigDict
import json
import datetime
from services.obs_conn import log_observability

class Viagem(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    DT_OPERACIONAL: Optional[float] = Field(None)
    ID_LINHA: Optional[int] = Field(None)
    TX_DESCR_LINHA: Optional[str] = Field(None)
    TX_COR_LINHA: Optional[str] = Field(None)
    NR_ORDEM: Optional[int] = Field(None)
    TX_PREFIXO: Optional[str] = Field(None)
    DT_INI_VIAGEM: Optional[float] = Field(None)
    DT_FIM_VIAGEM: Optional[float] = Field(None)
    DT_ATUALIZA: Optional[float] = Field(None)
    NR_DURACAO: Optional[float] = Field(None)
    ID_ORIGEM: Optional[float] = Field(None)
    ID_DESTINO: Optional[float] = Field(None)
    TX_ORIGEM: Optional[str] = Field(None)
    TX_DESTINO: Optional[str] = Field(None)
    TX_COMPOSICAO: Optional[str] = Field(None)
    ID_ORIGEM_PROG: Optional[str] = Field(None)
    TX_ORIGEM_PROG: Optional[str] = Field(None)
    ID_DESTINO_PROG: Optional[str] = Field(None)
    TX_DESTINO_PROG: Optional[str] = Field(None)
    DT_INI_VIAGEM_PROG: Optional[float] = Field(None)
    DT_FIM_VIAGEM_PROG: Optional[float] = Field(None)
    NR_OCORR_SIC: Optional[float] = Field(None)
    NR_CCO_SIC: Optional[float] = Field(None)
    NR_ANO_SIC: Optional[float] = Field(None)
    NR_DURACAO_REAL: Optional[float] = Field(None)
    NR_DURACAO_PROG: Optional[float] = Field(None)
    TX_TP_GRAFICO: Optional[str] = Field(None)
    TX_TP_DIA: Optional[str] = Field(None)
    FL_CONSIDERAR: Optional[float] = Field(None)
    TX_IPPM: Optional[str] = Field(None)
    TX_FPPM: Optional[str] = Field(None)
    TX_IPPT: Optional[str] = Field(None)
    TX_FPPT: Optional[str] = Field(None)
    TX_PICO: Optional[str] = Field(None)

    @model_validator(mode='before')
    def handle_nulls_and_cast(cls, values):
        for field_name, value in values.items():
            if pd.isna(value):
                values[field_name] = None
                continue

            if field_name in [
                'DT_OPERACIONAL', 'DT_INI_VIAGEM', 'DT_FIM_VIAGEM', 
                'DT_ATUALIZA', 'DT_INI_VIAGEM_PROG', 'DT_FIM_VIAGEM_PROG', 
                'NR_OCORR_SIC'
            ]:
                datetime_value = pd.to_datetime(value, errors='coerce')
                values[field_name] = datetime_value.timestamp() if not pd.isna(datetime_value) else None

            elif field_name in ['ID_LINHA', 'NR_ORDEM']:
                try:
                    values[field_name] = int(value)
                except (ValueError, TypeError):
                    values[field_name] = None

            elif field_name in ['ID_ORIGEM', 'ID_DESTINO', 'FL_CONSIDERAR', 'NR_CCO_SIC', 'NR_ANO_SIC']:
                try:
                    values[field_name] = float(value)
                except (ValueError, TypeError):
                    values[field_name] = None
                    
        return values

class Transform:
    def __init__(self, data_path, name_table):
        self.data_path = data_path
        self.df = pd.read_parquet(data_path)
        self.df = self.df.sample(frac=1)
        self.viagens = []
        self.name_table = name_table

    def transform_data(self):
        start_time = datetime.datetime.utcnow()
        print("Starting data transformation for Viagem...")

        for idx, row in enumerate(self.df.iterrows(), start=1):
            _, row_data = row
            row_dict = row_data.to_dict()
            try:
                viagem_json = json.dumps(Viagem(**row_dict).model_dump())
                self.viagens.append(viagem_json)
                
                if idx % 10000 == 0:
                    print(f"{idx} records transformed...")
            except Exception as e:
                print(f"Error processing row {idx}: {e}")

        end_time = datetime.datetime.utcnow()
        details = {
            "status": "success",
            "records_transformed": len(self.viagens)
        }
        
        log_observability("PCD Transform", start_time, end_time, details, name_table=self.name_table)
        print(f"Transformation completed. {len(self.viagens)} trips transformed.")
        return self.viagens