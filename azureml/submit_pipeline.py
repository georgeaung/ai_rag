from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import CommandJob

# AzureML credentials and workspace
client = MLClient(
    DefaultAzureCredential(),
    subscription_id="<your-subscription-id>",
    resource_group_name="<your-resource-group>",
    workspace_name="<your-workspace>"
)

# Define a command job that runs a Python script
job = CommandJob(
    code="./",
    command="python tests/test_pipeline.py",
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1",
    compute="cpu-cluster",
    display_name="ai-test-pipeline"
)

client.jobs.create_or_update(job)
