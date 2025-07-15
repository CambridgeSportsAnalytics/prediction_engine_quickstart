"""
Example script demonstrating how to directly interact with the CSA Prediction Engine API
using raw HTTP requests via the `requests` library.

This bypasses the Python API client and shows how to:
- Construct and POST a prediction job to the CSA engine
- Poll for results using job ID and job code

This method is useful for environments where you want full control over the request/response cycle.

Resources:
- CSA Prediction Engine API: https://docs.csanalytics.io/
"""

import requests
import json
import time
from generate_data import get_multi_theta_dataset

# CSA Prediction Engine API endpoints
PREDICTION_URL = 'https://api.csanalytics.io/v2/prediction-engine/grid'
RESULTS_URL = 'https://api.csanalytics.io/v2/prediction-engine/results'

# Authentication credentials (replace with your actual values)
ACCESS_ID = "YOUR_ACCESS_ID"  # Your personal access ID
API_KEY = "ORG_API_KEY"  # Organization-level API key

# Step 1: Generate synthetic dataset for prediction (endpoint accepts single theta prediction requests)
# - 1 prediction task
# - 5 features
# - 100 observations 
y, X, theta = get_multi_theta_dataset(
    num_tasks=1,
    num_variables=5,
    num_observations=100
)

# Step 2: Construct payload for prediction job submission
payload = {
    "y": y.tolist(),
    "X": X.tolist(),
    "theta": theta.tolist(),
    "access_id": ACCESS_ID  # Required for user authentication
}

# Optional: Print the payload for debugging
print("Submitting payload to CSA Prediction Engine:")
print(json.dumps(payload, indent=2))

# HTTP headers for POST request
headers = {
    'x-api-key': API_KEY,
    'Content-Type': 'application/json',
    'Connection': 'keep-alive'
}

# Step 3: Submit the prediction job
response = requests.post(PREDICTION_URL, headers=headers, data=json.dumps(payload))
job_response = response.json()
print("Submission response:")
print(json.dumps(job_response, indent=2))

# Extract job metadata (job_id and job_code)
job_id = job_response.get("job_id")
job_code = job_response.get("job_code")

# Optional: Add wait time to give server time to process predictions
print("\nWaiting for server to process job...")
time.sleep(15)

# Step 4: Poll for prediction results using job ID and job code
result_payload = {
    "job_id": job_id,
    "job_code": job_code
}

# Reuse headers for GET request
response = requests.get(RESULTS_URL, headers=headers, data=json.dumps(result_payload))
results = response.json()

# Step 5: Print the prediction results
print("\nPrediction results:")
print(json.dumps(results, indent=2))
