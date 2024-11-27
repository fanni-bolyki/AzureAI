from azure.ai.ml.entities import Data
from azure.identity import DefaultAzureCredential
from ml_client import my_ml_client_setup
import config as config

credential = DefaultAzureCredential()

def upload_csv_as_data_asset(ml_client, file_path, data_asset_name):
    print(f"Uploading {file_path} as a data asset...")
    data_asset = Data(
        name=data_asset_name,
        version="1",
        type="uri_file",
        path=file_path,
        description="Uploaded CSV file"
    )
    ml_client.data.create_or_update(data_asset)
    print(f"Data asset '{data_asset_name}' has been uploaded.")

if __name__ == "__main__":
    local_csv_file = config.local_csv_path
    new_data_asset_name = config.contract_with_sourcing_dataset_name
    ml_client = my_ml_client_setup()
    upload_csv_as_data_asset(ml_client, local_csv_file, new_data_asset_name)
