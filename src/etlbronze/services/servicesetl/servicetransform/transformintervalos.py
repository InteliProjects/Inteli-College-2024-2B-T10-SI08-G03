import pandas as pd
import datetime
import json
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ConfigDict
from ....services.obs_conn import log_observability


class Intervals(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    DT_HORA_MINUTO: Optional[int] = Field(None)
    ID_DT_HORA_MINUTO: Optional[int] = Field(None)
    HORA_INI: Optional[int] = Field(None)
    HORA_FIM: Optional[int] = Field(None)
    DURATION_MINUTES: Optional[float] = Field(None)

    @model_validator(mode='before')
    def handle_nulls_and_cast(cls, values):
        for field_name, value in values.items():
            if pd.isna(value):
                values[field_name] = None
            elif field_name in ['DT_HORA_MINUTO', 'HORA_INI', 'HORA_FIM']:
                try:
                    timestamp = pd.to_datetime(value, errors='coerce')
                    values[field_name] = int(timestamp.timestamp()) if not pd.isna(timestamp) else None
                except (ValueError, TypeError):
                    values[field_name] = None
            elif field_name == 'DURATION_MINUTES':
                try:
                    values[field_name] = float(value)
                except (ValueError, TypeError):
                    values[field_name] = None
        return values


class Transform:
    def __init__(self, data_path, name_table):
        print("Starting data transformation...")
        self.data_path = data_path
        self.name_table = name_table
        self.df = pd.read_parquet(data_path)
        self.intervals = []

    def transform_data(self):
        start_time = datetime.datetime.utcnow()

        for _, row in self.df.iterrows():
            row_dict = row.to_dict()
            row_dict['name_table'] = self.name_table

            for field, value in row_dict.items():
                if isinstance(value, pd.Timestamp):
                    row_dict[field] = value.isoformat()

            try:
                interval_json = json.dumps(row_dict)
                self.intervals.append(interval_json)
            except Exception as e:
                print(f"Error transforming row {row.name}: {e}")

        end_time = datetime.datetime.utcnow()

        details = {
            "status": "success",
            "records_transformed": len(self.intervals),
            "table_name": self.name_table
        }
        log_observability("Transform", start_time, end_time, details, self.name_table)

        print(f"Transformation completed. {len(self.intervals)} intervals transformed.")
        return self.intervals