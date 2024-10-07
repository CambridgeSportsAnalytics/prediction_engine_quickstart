# Prediction Engine

Welcome to Cambridge Sports Analytics' **Prediction Engine** repository. This repository is a simple, hands-on reference for developers looking to interact with our **Prediction Engine API**. 

The examples provided in this repository aim to help you understand how to construct and send HTTPS requests to the Prediction Engine API correctly. It is intended to give you a clear and practical understanding of the request/response flow.

## Contents

- [end_points](end_points): This folder contains code examples for each of the available API endpoints, showing how to make HTTPS requests and receive responses from the Prediction Engine API in Python. 

## Using This Repository

Begin by cloning the repository to your local machine:

```git clone https://github.com/CambridgeSportsAnalytics/prediction_engine.git```

Before running the examples provided in this repository check your:

1. **API Credentials**: You must have valid API credentials, including an `CSA_API_KEY` and a `CSA_ACCESS_ID` provided by the CSA team to authenticate requests to the Prediction Engine. These variables should be set as part of your environment variables.
2. **Python Environment**: pip install -r requirements.txt after cloning the repo. 

## Additional Notes

Please note that our example scripts are making  **single** prediction calls to our prediction endpoints. If you'd like to make many calls to our API more easily, unpack results automatically and integrate results fetching by default, we suggest that you pip install the prediction engine python package. 

## License

(c) 2023 - 2024 Cambridge Sports Analytics, LLC. All rights reserved.
