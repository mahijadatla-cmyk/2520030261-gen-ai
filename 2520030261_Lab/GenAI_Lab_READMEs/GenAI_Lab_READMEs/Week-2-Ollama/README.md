# Week 2 – Ollama

## Aim
Run a language model locally with Ollama and connect to it from the Week 2 Python experiment.

## Requirements
- Ollama installed on the computer
- A model downloaded through Ollama
- Python
- The Python packages required by the Week 2 script

## Check Ollama
Open PowerShell or the VS Code terminal and check that Ollama is installed:

```powershell
ollama --version
```

List the models already downloaded:

```powershell
ollama list
```

If the Ollama service is not running, start it using the Ollama application or the command appropriate for your installation.

## Download and run a model
Use the model name specified by your Week 2 lab instructions or Python script:

```powershell
ollama pull MODEL_NAME
ollama run MODEL_NAME
```

Replace `MODEL_NAME` with the exact model name selected for your experiment. Do not type the placeholder literally.

## Run the Python experiment
Open this folder in VS Code, activate the environment used by your lab, install the packages listed in the folder's `requirements.txt` (if present), and run the Python script provided for Week 2:

```powershell
pip install -r requirements.txt
python main.py
```

If your Week 2 script has a different filename, run that filename instead.

## Expected result
Ollama should load the selected local model and return a response to the prompt sent by the experiment.

## Troubleshooting
- `ollama` is not recognized: install Ollama and reopen the terminal.
- Model not found: check the exact model name with `ollama list` and pull the required model.
- Connection refused: make sure the Ollama service is running.
- Slow first response: the model may need to load into memory; model size and computer resources affect speed.

## Note
This README uses placeholders because the Week 2 script and exact model name were not visible in the supplied folder screenshot. Replace them with the exact values used in your experiment.
