# Prediction Engine

Welcome to the **Prediction Engine** repository. This repository is a simple, hands-on reference for developers looking to interact with our **Prediction Engine API**. 

The examples provided in this repository aim to help you understand how to construct and send HTTP requests to the Prediction Engine API correctly. It is intended to give you a clear, practical understanding of the request/response flow.

## Contents

- [Endpoints](Endpoints): This folder contains code examples for each of the available API endpoints, showing how to make HTTP requests and receive responses from the Prediction Engine API in Python. 

## Using This Repository

Begin by cloning the repository to your local machine:

```git clone https://github.com/CambridgeSportsAnalytics/prediction_engine.git```

Before running the examples provided in this repository check your:

1. **API Credentials**: You must have valid API credentials, including an `CSA_API_KEY` and a `CSA_ACCESS_ID` provided by the CSA team to authenticate requests to the Prediction Engine. We recommend that you set these in a .env file.
2. **Python Environment**: pip install -r requirements.txt after cloning the repo. 

## Additional Notes

Please note that our example scripts are making  **single** prediction calls to our prediction endpoints. If you'd like to make many calls to our API more easily, unpack results automatically and integrate results fetching by default, we suggest that you pip install the prediction engine python package. 

## License

(c) 2023 - 2024 Cambridge Sports Analytics, LLC. All rights reserved.
