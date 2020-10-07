./.env/scripts/activate.ps1

$date = Get-Date -Format "yyyyMMddHHmmss"
$distpath = '.\dist\windows\build_' + $date

pyinstaller --log-level=WARN `
	--workpath .build `
	--distpath $distpath `
	--noconfirm `
	--onefile `
	tao.spec

deactivate
