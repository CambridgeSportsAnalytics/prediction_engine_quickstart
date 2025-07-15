"""
Example script demonstrating how to use the CSA Python API client to interact with
the CSA Prediction Engine for submitting and managing predictive modeling tasks.

This client library handles:
- Job creation and submission to the remote CSA engine
- Multi-threaded POST requests for parallel task execution
- Automatic polling for job completion and result retrieval

Resources:
- CSA Python API Client: https://docs.csanalytics.io/python-api-package/api-client
- CSA Prediction Engine Documentation: https://docs.csanalytics.io/
"""

import os
import numpy as np
from generate_data import get_multi_theta_dataset
from multiprocessing import freeze_support

from csa_prediction_engine import predict_grid, GridOptions, PredictionResults

def main():
    """
    Main entry point for submitting prediction tasks to the CSA Prediction Engine.

    Steps:
    1. Set CSA API credentials.
    2. Generate synthetic multivariate input data.
    3. Define grid prediction options.
    4. Submit predictions using CSA's multi-threaded API client.
    5. Collect and display results.
    """


    # Set credentials for CSA API access (replace with your own access IDs)
    os.environ['CSA_ACCESS_ID'] = 'YOUR_ACCESS_ID'      # Private user token
    os.environ['CSA_API_KEY'] = 'ORG_API_KEY'         # Organization token
    
    # Generate synthetic dataset: 3 tasks, 5 features, 200 observations
    y, X, theta = get_multi_theta_dataset(num_tasks=3, num_variables=5, num_observations=200)

    # Construct prediction options
    # See also https://docs.csanalytics.io/python-api-package/csa-common-lib/prediction-options
    PredictionOptions = GridOptions()

    # Submit predictions using the CSA Grid prediction engine
    # - Sends POST requests to the server for each task
    # - Uses multi-threading to parallelize submission
    # - Polls CSA backend for results and blocks until completion
    yhat, output_details = predict_grid(y=y, X=X, theta=theta, Options=PredictionOptions)

    # Wrap results in a helper class for easier downstream use
    Results = PredictionResults(output_details)

    # Display predictions and metadata
    Results.display()

    # Alternatively, display the raw data
    print("Predictions:", yhat)
    print("Output details:", output_details)

    # Optionally: save `results` to disk for future analysis
    # (Not implemented here — recommended for reproducibility)

if __name__ == '__main__':

    # Required to safely launch multi-threaded code
    freeze_support()
    
    # Run the program
    main()
