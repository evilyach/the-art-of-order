#!/bin/bash

source .env/bin/activate

isort src
black src

deactivate