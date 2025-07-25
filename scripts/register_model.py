import mlflow
from mlflow.tracking import MlflowClient
import os
from datetime import datetime
from pathlib import Path



# Set the tracking URI if it's not the default
mlflow.set_tracking_uri(os.getenv('MLFLOW_URL', 'http://localhost:5000'))

client = MlflowClient()

# Replace with your actual run ID and model artifact path
run_id = os.getenv('RUN_ID', 'run_id not found')
model_name =  os.getenv("MODEL_NAME", "no_name")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"
model_artifact_path = MODEL_DIR / "model.pkl"

# Register the model
result = mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name=model_name
)

# Optionally, you can wait until the model is ready
client.transition_model_version_stage(
    name=model_name,
    version=result.version,
    stage="Staging"
)


client.set_registered_model_alias(model_name, "champion", result.version)