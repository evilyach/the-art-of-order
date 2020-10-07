#!/bin/bash -e
# https://github.com/cdrx/docker-pyinstaller

pip install tao-0.1.0-py3-none-any.whl

pyinstaller \
    --onefile \
    --clean \
    tao.py
