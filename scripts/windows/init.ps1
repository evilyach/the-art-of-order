# Creating virtual environment
python.exe -m venv .env

./.env/scripts/activate.ps1

# Installing system dependencies
.\.env\Scripts\python.exe -m pip install "pip==20.2.3" `
    "poetry==1.1.0"

# Installing dependencies specified in pyproject.toml file
.\.env\Scripts\python.exe -m poetry install

# Post-install handling
deactivate
