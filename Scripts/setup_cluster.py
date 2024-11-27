import config
from azure.ai.ml.entities import AmlCompute
from ml_client import my_ml_client_setup

compute_name = config.compute_name

# Define compute cluster parameters
compute_cluster = AmlCompute(
    name=compute_name,
    size="STANDARD_DS3_V2",  # VM type
    min_instances=0,         # Minimum nodes
    max_instances=4,         # Maximum nodes
    idle_time_before_scale_down=120  # Time in seconds before scaling down
)

ml_client = my_ml_client_setup()

# # Create the compute cluster
# compute_cluster = ml_client.compute.begin_create_or_update(compute_cluster)
# print(f"Compute cluster '{compute_name}' creation initiated.")

# Delete the compute cluster
ml_client.compute.begin_delete(compute_name)
print(f"Compute cluster '{compute_name}' deletion initiated.")

