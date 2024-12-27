import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import clickhouse_connect

# Class for connecting to AWS S3
class AwsConn:
    def __init__(self):
        load_dotenv()
        self.aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY') 
        self.aws_region = os.getenv('AWS_REGION')
        self.bucket_name = os.getenv('AWS_BUCKET')
        self.aws_session_token = os.getenv('AWS_SESSION_TOKEN')
        
        self.click_house_host = os.getenv('CLICKHOUSE_HOST')
        self.click_house_port = os.getenv('CLICKHOUSE_PORT')
        self.click_house_user = os.getenv('CLICKHOUSE_USER')
        self.click_house_password = os.getenv('CLICKHOUSE_PASSWORD')
        
        
        if not all([self.aws_access_key_id, self.aws_secret_access_key, self.aws_region, self.bucket_name]):
            raise ValueError("Incomplete S3 credentials or configuration.")
        try:
            self.client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                aws_session_token= self.aws_session_token,
                region_name=self.aws_region
            )
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError(f"Error setting credentials: {e}")

    def send_to_s3(self, key, folder, file):
        print(self.bucket_name)
        try:
            self.client.upload_file(file, self.bucket_name, f'{folder}/{key}')
            return f'{folder}/{key}'
        except Exception as e:
            raise RuntimeError(f"Error uploading file to S3: {e}")
        
        
    def load_from_s3(self, key, download_dir='data'):
        os.makedirs(download_dir, exist_ok=True)
        
        local_file_path = os.path.join(download_dir, os.path.basename(key))
        
        try:
            self.client.download_file(self.bucket_name, key, local_file_path)
            print(f"File downloaded to {local_file_path}")
            return local_file_path
        except Exception as e:
            raise RuntimeError(f"Error downloading file from S3: {e}")
        
    def send_to_clickhouse(self, table_name, data):
        try:
            client = clickhouse_connect.get_client()
            
            query = f"CREATE TABLE IF NOT EXISTS {table_name} Engine = MergeTree ORDER BY (id)"
            client.execute(query)
            print(f"Table {table_name} created")
        except Exception as e:
            raise RuntimeError(f"Error creating table in ClickHouse: {e}")
        
        data_line = data['data_line']
        data_tags = data['data_tags']
        data_ingestao = data['data_ingestao']

        query = f"INSERT INTO {table_name} VALUES "
        for i in range(len(data_line)):
            query += f"({data_line[i]}, '{data_tags[i]}', '{data_ingestao[i]}'),"
        query = query[:-1]
        
        try:
            client.execute(query)
            print(f"Data inserted into {table_name}")
        except Exception as e:
            raise RuntimeError(f"Error inserting data into ClickHouse: {e}")
        
        