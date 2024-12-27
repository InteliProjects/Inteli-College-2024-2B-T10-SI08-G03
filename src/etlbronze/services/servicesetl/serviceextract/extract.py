import os
import datetime
from ....services.aws_conn import AwsConn
from ....services.obs_conn import log_observability

class Extract:
    def __init__(self):
        pass

    def save_data(self, key):
        start_time = datetime.datetime.utcnow()
        aws = AwsConn()
        print("entrou")
        print(" ")
        print(key)

        directory = os.path.dirname(key)
        file_name = os.path.basename(key)
        name_table = os.path.basename(directory) if directory else None

        if not name_table:
            raise ValueError(f"Invalid key structure: '{key}'. Unable to extract name_table.")

        print(directory)
        print(file_name)
        print(name_table)

        try:
            file_path = aws.load_from_s3(key)  # Ensure this function returns a valid file path.
            data_tag = f"{name_table}_{file_name.split('.')[0]}"
            end_time = datetime.datetime.utcnow()
            details = {
                "status": "success",
                "file_path": file_path,
                "data_tag": data_tag
            }
            log_observability("Extract", start_time, end_time, details, name_table)
            print(name_table)
            return file_path, data_tag, name_table
        except Exception as e:
            end_time = datetime.datetime.utcnow()
            details = {
                "status": "error",
                "error_message": str(e)
            }
            log_observability("Extract", start_time, end_time, details, name_table if name_table else "unknown")
            print("error downloading file from S3", e)
            raise RuntimeError(f"Error downloading file from S3: {e}")