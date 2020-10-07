./.env/scripts/activate.ps1

pyinstaller --log-level=WARN `
	--workpath .build `
	--noconfirm `
	--onefile `
	tao.spec

deactivate