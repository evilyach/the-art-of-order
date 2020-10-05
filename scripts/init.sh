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

# Installing dependencies for virtual environment
pip install "pip==20.0.2"

# Post-install handling
deactivate
