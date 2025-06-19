# Azure ML Integration – Insurance AI Explainer

## Components

- `submit_pipeline.py`: Programmatic SDK-based submission to Azure ML
- `insurance_ai_test_job.yml`: YAML definition for no-code/GUI submission

## How to Use the YAML Job File

1. Ensure you have Azure CLI and ML extension installed:
```bash
az extension add -n ml
```

2. Log in and set workspace:
```bash
az login
az account set --subscription <your-subscription-id>
az configure --defaults group=<your-rg> workspace=<your-ws>
```

3. Submit the job:
```bash
az ml job create --file azureml/ai_test_job.yml
```

## Registering as a Reusable Component

You can define a component from this script using a component YAML like:
```yaml
name: run-ai-explainer
inputs:
  policy_id: {type: string, default: "12345"}
command: >
  python -c "from insurance_ai_rag.pipeline import run_pipeline; print(run_pipeline('${{inputs.policy_id}}'))"
code: ../
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1
```

Then submit:
```bash
az ml component create --file component.yml
```
