subscription_id = "b6b625de-1867-4440-84ca-40d597bce03f"
resource_group = "MOG-SWCT-PROCML-RG01"
workspace_name = "MOG-SWCT-PROCML-MLW03"
compute_name = "automl-compute-cluster"

# Machine Learning dataset configuration
local_csv_path = "C:/Users/FBolyki/Code/procurement-data-science-initiative/sourcing_history_generator/contract_with_sourcing_history_only_no_dupl.csv" 
contract_with_sourcing_dataset_name = "contract_with_sourcing_history_FULL"
target_column = "Sourcing_history-Sourcing lead-time"

# OpenAI configuration
endpoint = "https://mog-swct-procml-oai01.openai.azure.com/"

deployment_id = "gpt-4o"
deployment_api_version = "2024-08-01-preview"

embedding_model = "text-embedding-ada-002"
embedding_api_version = "2023-05-15"
embedding_uri = "https://mog-swct-procml-oai01.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15"