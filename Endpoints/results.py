import os
import json
import requests


# Specify the PSR model endpoint 
url = 'https://api.csanalytics.io/v2/results'

# Define the headers 
headers= {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'x-api-key': os.getenv('CSA_API_KEY')
        }
        
# Construct input payload
payload = {
            "job_id": 9433,
            "job_code": "f020dba22ca42e0f"
          }

# Convert payload dictionary into a json request body
json_payload = json.dumps(payload)

response = requests.get(url, data=json_payload, headers=headers)

# Print the response content if the request is successful
if response.status_code == 200:
    response_body = json.loads(response.text)
    print("Prediction Value (yhat):", response_body['yhat']) # Access your predicted value (yhat)
    print("Available Keys:", response_body.keys()) # All of the available parameters you can access in your results
else:
    print("Unsuccessful post request:", response.text, response.status_code)