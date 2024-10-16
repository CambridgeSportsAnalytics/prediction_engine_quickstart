import os
import json
import requests


# Specify the Grid model endpoint 
url = 'https://api.csanalytics.io/v2/prediction-engine/grid'

# Define the headers 
headers= {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'x-api-key': os.getenv('CSA_API_KEY')
        }
        
# Construct input payload
payload = {
            "access_id": os.getenv('CSA_ACCESS_ID'),
            "y":
                [[0.5],
                 [3.2],
                 [0.6]],
            "X":
                [[28.0, 1.0, 84.6,],
                 [20.0, 8.1, 16.4],
                 [11.0, 7.0, 59.7]],
            "theta":
                [[25.0, 6.2, 33.7]]
}

# Set your maxfit prediction options. Model defaults to these values if none are provided
prediction_options = {
            'threshold': [0],
            'is_threshold_percent': True,
            'most_eval': True,
            'eval_type': 'both',
            'adj_fit_multiplier': 'K',
            'cov_inv': None,
            'threshold': None,
            'threshold_range': [0, 0.20, 0.50, 0.80],
            'stepsize': 0.20,
            'objective': 'adjusted_fit',
            'attribute_combi': None,
            'k': 1,
}

# Merge the options dictionary into the payload 
payload.update(prediction_options)

# Convert payload dictionary into a json request body
json_payload = json.dumps(payload)

response = requests.post(url, data=json_payload, headers=headers)

# Print the response content if the request is successful
if response.status_code == 200:
    response_body = json.loads(response.text)
    print("Job id:", response_body['job_id']) # Job id (used to reference your prediction request)
    print("Job code:", response_body['job_code']) # Job code (used to reference your prediction request)
else:
    print("Unsuccessful post request:", response.text, response.status_code)