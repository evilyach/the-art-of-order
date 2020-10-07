#!/bin/bash

# Defining variables
VENV_DIR=".env"
IMPLEMENTATION="python3"

# Creating and(or) entering virtual environment
if [ ! -d "$VENV_DIR" ]; then
	"$IMPLEMENTATION" -m venv "$VENV_DIR"
fi

echo "Trying to enter venv at $VENV_DIR"
source "$VENV_DIR"/bin/activate
echo "Successfully entered"

# Installing system dependencies
pip install "pip==20.2.3" \
	"poetry==1.1.0"

# Installing dependencies specified in pyproject.toml file
poetry install

# Post-install handling
deactivate
