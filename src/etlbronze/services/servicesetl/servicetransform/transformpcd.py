import pandas as pd
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ConfigDict
import json
import datetime
from services.obs_conn import log_observability

class PcdData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    dt_destination: Optional[float] = Field(None, alias='Dt Destino')
    dt_operational: Optional[float] = Field(None, alias='Dt Operacional')
    dt_origin: Optional[float] = Field(None, alias='Dt Origem')
    alert_flag: Optional[int] = Field(None, alias='Fl Alerta')
    pcd_groups: Optional[str] = Field(None, alias='Grupos PCD')
    car_id: Optional[int] = Field(None, alias='Id Carro')
    alert_station_id: Optional[int] = Field(None, alias='Id Estacao Alerta')
    destination_station_id: Optional[int] = Field(None, alias='Id Estacao Destino')
    origin_station_id: Optional[int] = Field(None, alias='Id Estacao Origem')
    record_id: Optional[int] = Field(None, alias='Id Registro')
    line_description: Optional[str] = Field(None, alias='Tx Descr Linha')
    destination_station: Optional[str] = Field(None, alias='Tx Estacao Destino')
    line: Optional[str] = Field(None, alias='Tx Linha')
    observation: Optional[str] = Field(None, alias='Tx Obs')
    door_number: Optional[int] = Field(None, alias='Tx Porta')
    prefix: Optional[str] = Field(None, alias='Tx Prefixo')
    pcd_type: Optional[str] = Field(None, alias='Tx Tipo Pcd')
    train_id: Optional[str] = Field(None, alias='Tx Trem')
    destination_username: Optional[str] = Field(None, alias='Tx Username Destino')
    origin_username: Optional[str] = Field(None, alias='Tx Username Origem')

    @model_validator(mode='before')
    def handle_nulls_and_cast(cls, values):
        for field_name, field in cls.model_fields.items():
            field_alias = field.alias or field_name
            value = values.get(field_alias, None)

            if pd.isna(value):
                values[field_alias] = None
                continue

            if field_name in ['dt_destination', 'dt_operational', 'dt_origin']:
                values[field_alias] = pd.to_datetime(value, errors='coerce')
                if pd.isna(values[field_alias]):
                    values[field_alias] = None
                else:
                    values[field_alias] = int(values[field_alias].timestamp())
            elif field_name in [
                'alert_flag', 'car_id', 'alert_station_id',
                'destination_station_id', 'origin_station_id',
                'record_id', 'door_number'
            ]:
                try:
                    values[field_alias] = int(value)
                except (ValueError, TypeError):
                    values[field_alias] = None
            elif field_name in [
                'pcd_groups', 'line_description', 'destination_station',
                'line', 'observation', 'prefix', 'pcd_type',
                'train_id', 'destination_username', 'origin_username'
            ]:
                values[field_alias] = str(value)
        return values

class Transform:
    def __init__(self, data_path, name_table):
        self.data_path = data_path
        self.name_table = name_table
        self.data = self._load_data()

    def _load_data(self):
        """Carrega os dados do arquivo parquet."""
        return pd.read_parquet(self.data_path)

    def transform_data(self):
        """Transforma os dados brutos em um formato processado."""
        print(f"Dimensões iniciais: {self.data.shape}")
        
        colunas_criticas = ['Dt Destino', 'Dt Operacional', 'Dt Origem', 'Id Registro']
        self.data.dropna(subset=colunas_criticas, inplace=True)
        print(f"Após remover nulos nas colunas críticas: {self.data.shape}")
        
        for col in ['Dt Destino', 'Dt Operacional', 'Dt Origem']:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
        self.data.dropna(subset=['Dt Destino', 'Dt Operacional', 'Dt Origem'], inplace=True)
        print(f"Após validar datas: {self.data.shape}")
        
        self.data = self.data[self.data['Fl Alerta'].isin([0, 1])]
        print(f"Após filtrar Fl Alerta: {self.data.shape}")
        
        colunas_inteiras = [
            'Id Carro', 'Id Estacao Alerta', 'Id Estacao Destino',
            'Id Estacao Origem', 'Id Registro', 'Tx Porta'
        ]
        for col in colunas_inteiras:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            print(f"Valores válidos na coluna {col}: {self.data[col].notnull().sum()}")
        self.data.dropna(subset=colunas_inteiras, inplace=True)
        print(f"Após validar colunas inteiras: {self.data.shape}")
        
        return self.data

