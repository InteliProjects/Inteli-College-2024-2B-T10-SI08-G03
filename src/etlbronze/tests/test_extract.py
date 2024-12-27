import pytest
from unittest.mock import patch, MagicMock
from etlbronze.services.servicesetl.serviceextract.extract import Extract


def test_save_data_success():
    
    mock_key = "bucket_name/folder_name/table_name/file.csv"
    mock_file_path = "/local/path/to/file.csv"
    mock_data_tag = "table_name_file"
    mock_name_table = "table_name"

    mock_aws = MagicMock()
    mock_aws.load_from_s3.return_value = mock_file_path

    with patch("etlbronze.services.servicesetl.serviceextract.extract.AwsConn", return_value=mock_aws):
        with patch("etlbronze.services.servicesetl.serviceextract.extract.log_observability") as mock_log:
            extract = Extract()

            result = extract.save_data(mock_key)

            assert result == (mock_file_path, mock_data_tag, mock_name_table)
            mock_aws.load_from_s3.assert_called_once_with(mock_key)
            mock_log.assert_called_once()
            log_args = mock_log.call_args[0]
            assert log_args[0] == "Extract"
            assert log_args[3]["status"] == "success"

def test_save_data_error():
    mock_key = "file.csv" 
    mock_error_message = f"Invalid key structure: '{mock_key}'. Unable to extract name_table."

    with patch("etlbronze.services.servicesetl.serviceextract.extract.AwsConn"), \
         patch("etlbronze.services.servicesetl.serviceextract.extract.log_observability") as mock_log:
        
        extract = Extract()

        with pytest.raises(ValueError, match=mock_error_message):
            extract.save_data(mock_key)
        mock_log.assert_not_called()


