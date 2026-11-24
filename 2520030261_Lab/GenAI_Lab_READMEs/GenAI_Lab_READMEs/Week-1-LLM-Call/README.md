# Week 1 – LLM Call

## Aim
Connect a Python program to a hosted Large Language Model (LLM) and print its response.

## Files
- `main.py` – sends a prompt to the Gemini API and displays the response.
- `.env` – stores the API key (do not upload or share this file).
- `.gitignore` – excludes files that should not be committed.

## Requirements
- Python
- Internet connection
- A Gemini API key with an enabled project/API
- Python package: `google-genai`

## Setup
Open the terminal in this folder. Activate the lab virtual environment from the repository root:

```powershell
..\.myenv\Scripts\Activate.ps1
```

Install the package:

```powershell
pip install google-genai python-dotenv
```

If the project already has a `requirements.txt`, use `pip install -r requirements.txt` instead.

## API key
Add your key to the `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never paste the real key into source code or screenshots. Make sure `main.py` loads the `.env` file (for example, with `python-dotenv`) before reading `GEMINI_API_KEY`.

## Run

```powershell
python main.py
```

The program sends its prompt to the configured Gemini model and prints the model's text response.

## Troubleshooting
- If the key is reported as `NOT SET`, check the `.env` filename, its location, and whether the program loads it.
- If the API returns a 403/billing or project-access error, check the API key's Google project and API/billing access.
- If a model returns 404, check that the model name is currently available to your account.
- If PowerShell blocks activation, use the execution-policy instructions approved for your machine or activate the environment from a supported terminal.
