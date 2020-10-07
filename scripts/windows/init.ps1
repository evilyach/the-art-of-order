# Creating virtual environment
python.exe -m venv .env

./.env/scripts/activate.ps1

# Get-Location

# Installing system dependencies
.\.env\Scripts\python.exe -m pip install "pip==20.2.3" `
    "poetry==1.1.0"

# Installing dependencies specified in pyproject.toml file
poetry install

# Post-install handling
deactivate