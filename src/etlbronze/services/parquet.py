import pandas as pd

class Converter:
    def __init__(self):
        pass
    
    def csv_to_parquet(self, csv_file):
        try:
            df = pd.read_csv(csv_file)
            df.to_parquet(csv_file.replace('.csv', '.parquet'))
        except Exception as e:
            raise RuntimeError(f"Error converting file to parquet: {e}")
        
    def df_to_parquet(self, df, file_name):
        try:
            df = self._adjust_column_types(df)
            df.to_parquet(file_name)
            print(f"DataFrame successfully saved to {file_name}")
        except Exception as e:
            raise RuntimeError(f"Error converting DataFrame to parquet: {e}")
        
    def xlsx_to_parquet(self, xlsx_file):
        try:
            df = pd.read_excel(xlsx_file)
            df.to_parquet(xlsx_file.replace('.xlsx', '.parquet'))
        except Exception as e:
            raise RuntimeError(f"Error converting file to parquet: {e}")
        
    def _adjust_column_types(self, df):
        for column in df.columns:
            if df[column].dtype == 'object':
                df[column] = df[column].astype(str)
        return df
