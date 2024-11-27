import config
from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential


def my_ml_client_setup():
    subscription_id = config.subscription_id
    resource_group = config.resource_group
    workspace_name = config.workspace_name    
    credential = AzureCliCredential()
    ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)
    return ml_client
