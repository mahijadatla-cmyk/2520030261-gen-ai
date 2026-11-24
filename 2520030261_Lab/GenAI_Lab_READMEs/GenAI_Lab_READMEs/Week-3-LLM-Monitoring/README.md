# Week 3 – LLM Monitoring

## Aim
Run the LLM client experiment with usage monitoring/logging. The folder contents indicate a client, a usage logger, a main program, and a test client.

## Files
- `main.py` – main experiment entry point.
- `llm_client.py` – LLM client code.
- `usage_logger.py` – usage logging component.
- `test_client.py` – test script for the client.
- `requirements.txt` – Python dependencies.
- `.env` – environment configuration/secrets; do not share it.
- `venv/` and `__pycache__/` – generated environment/cache folders.

## Setup
Open the Week 3 folder in VS Code. Activate its local virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Check `.env` and provide the environment variables required by `llm_client.py` and the monitoring/database configuration. Do not commit API keys or passwords.

## Run the experiment

```powershell
python main.py
```

## Run the client test

```powershell
python test_client.py
```

Run the test after configuring the required environment variables and any service/database used by the code.

## Expected result
The main program should call the configured LLM client. The monitoring/logger component should record the usage information implemented by the experiment. The test script should report whether the client test passes.

## Troubleshooting
- Missing environment variable: check the variable names expected in the Python files and set them in `.env`.
- Import error: activate `venv` and install `requirements.txt`.
- API error: verify the API key, model name, and provider access.
- Database/monitoring connection error: verify the service is running and the connection settings in `.env` are correct.
