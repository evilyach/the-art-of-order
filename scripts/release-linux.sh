#!/bin/bash

source ".env/bin/activate"

pyinstaller \
    --log-level=WARN \
    --workpath .build \
    --onefile \
    --nowindow \
    --clean \
    --dist ./dist/linux \
    src/tao.py

deactivate
