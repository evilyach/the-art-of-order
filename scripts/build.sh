#!/bin/bash

source .env/bin/activate

pyinstaller --log-level=WARN \
	--workpath .build \
	--noconfirm \
	--onefile \
	tao.spec

deactivate
