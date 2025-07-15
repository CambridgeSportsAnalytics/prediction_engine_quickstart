# CSA Prediction Engine - Quickstart Guide
[![PyPI version](https://img.shields.io/pypi/v/csa-prediction-engine.svg)](https://pypi.org/project/csa-prediction-engine/)
[![Python Version](https://img.shields.io/badge/python-%20v3.11-blue)](https://github.com/CambridgeSportsAnalytics/prediction_engine)
[![CodeFactor](https://www.codefactor.io/repository/github/cambridgesportsanalytics/prediction_engine/badge)](https://www.codefactor.io/repository/github/cambridgesportsanalytics/prediction_engine)
[![Total Lines of Code](https://tokei.rs/b1/github/CambridgeSportsAnalytics/prediction_engine?category=code)](https://github.com/CambridgeSportsAnalytics/prediction_engine)

This repository is a **quickstart reference and example suite** for analysts and developers working with the **CSA Prediction Engine API**. It includes:

🔹 Endpoint specifications (OpenAPI 3.0)  
🔹 Example scripts for each endpoint  
🔹 End-to-end workflows using both direct HTTP and the official pip package  
🔹 Sample data generation and result unpacking utilities  

## 📁 Repository Structure

```bash
.
├── docs/
│   └── api_specs/            # OpenAPI 3.0 JSON specs for each endpoint
├── endpoints/                # Python examples per endpoint
│   ├── grid.py
│   ├── grid_singularity.py
│   ├── maxfit.py
│   └── ...
├── workflows/                # End-to-end example workflows
│   ├── run_with_http.py      # Direct HTTP call workflow
│   ├── run_with_client.py    # Using the official CSA pip package
│   └── data_generation.py    # (Optional) Generates synthetic sample data
```

## 🚀 Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/CambridgeSportsAnalytics/prediction_engine.git
cd prediction_engine
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Set your CSA API Credentials

The examples require valid API creddentials:
```python
os.environ['CSA_ACCESS_ID'] = 'YOUR_ACCESS_ID'    # Private user token
os.environ['CSA_API_KEY'] = 'ORG_API_KEY'         # Organization token
```
>You must obtain these credentials from the CSA Team. We recommend storing them securely in environment variables or a `.env` file.


## 🧪 Example Workflows
Each script demonstrates:
- How to generate (or import) sample data
- How to call the CSA Prediction Engine via
  - Direct HTTP request (`requests`)
  - Official pip package client ([csa-prediction-engine](https://pypi.org/project/csa-prediction-engine/))
- How to unpack and interpret results

Run either workflow:
```bash
python workflows/run_with_http.py # Direct HTTP call
python workflows/run_with_client.py # PIP-installed client usage
```

## 📦 Key Files
| File | Description |
| :--- | :---|
| run_with_http.py | Makes raw HTTP calls using requests |
| run_with_client.py | Uses pip package to submit & manage jobs |
| data_generation.py | Synthetic data utility for input creation |
| endpoints/*.py | Endpoint-specific usage and response examples |
| docs/api_specs/ | OpenAPI specs for each endpoint (JSON format) |

## 🧊 Concurrency Notes and Cross-Platform Compatibility

This repository uses `from multiprocessing import freeze_support` to ensure cross-platform compatibility when using concurrency. This line is **required** on:

- **Windows**, which always uses the `spawn` start method
- **macOS with Apple Silicon** (M1/M2/M3/M4) when using Python installed via Homebrew, which also defaults to `spawn`

While it's a no-op on most Linux systems (which use `fork` by default), including `freeze_support()` ensures safe and consistent behavior across all platforms, especially when running our scripts and pip package that use multiprocessing or multi-threaded APIs.

### 🔁 Single vs Batch API Calls

The provided examples focus on single-call predictions for clarity and simplicity. For larger batch workflows (e.g. multiple prediction tasks / multiple prediction circumstances) with built-in result polling and multithreaded execution, we recommend using the official pip package:

```bash
pip install csa-prediction-engine
```

## 📖 Documentation
- 📘 [CSA Prediction Engine Overview](https://docs.csanalytics.io)
- 🐍 [CSA Python API Client Docs](https://docs.csanalytics.io/python-api-package/api-client)
- ⚙️ [Prediction Options Reference](https://docs.csanalytics.io/python-api-package/csa-common-lib/prediction-options)
 
## 📬 Support

Questions or issues? Please reach out to us 📧 support@csanalytics.io

## ⚖️ License

Copyright (c) 2023 - 2025 Cambridge Prediction Analytics, LLC. All rights reserved.
