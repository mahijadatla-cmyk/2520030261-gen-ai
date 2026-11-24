# Week 5 – Token Economics

## Aim
Study token-budget or token-cost calculations using the Python budget experiment in this folder.

## Files
- `budget.py` – budget/token-economics program.
- `test_budget.py` – tests for the budget program.
- `requirements.txt` – Python dependencies, if required by the experiment.
- `.env` – environment configuration, if used; do not share secrets.
- `__pycache__/` – generated Python cache folder.

## Setup
Open the Week 5 folder in VS Code. Activate the lab virtual environment from the repository root:

```powershell
..\.myenv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

If the requirements file is empty or no third-party packages are needed, use the imports in `budget.py` to identify the dependencies.

## Run the experiment

```powershell
python budget.py
```

## Run the tests

```powershell
python -m pytest test_budget.py
```

If `pytest` is not installed and the requirements file does not include it:

```powershell
pip install pytest
```

## Expected result
`budget.py` should display the calculations or budget information implemented in the experiment. The test file should show whether the budget-related test cases pass.

## Troubleshooting
- Import error: activate the correct environment and install dependencies.
- Test command not found: install `pytest` in the active environment.
- Unexpected calculation: compare the inputs and expected values in `test_budget.py` with the logic in `budget.py`.

## Note
The exact formulas, input format, and output fields depend on the code in `budget.py`; check that file when documenting the detailed calculation rules.
