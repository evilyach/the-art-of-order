# Creating virtual environment
python -m venv .env
./.env/scripts/activate.ps1

# Installing system dependencies
.\.env\Scripts\python.exe -m pip install "pip==20.3.3"

# Installing dependencies specified in requirements.txt file
.\.env\Scripts\python.exe -m pip install -r .\requirements.txt

# Post-install handling
deactivate
