./.env/scripts/activate.ps1

$date = Get-Date -Format "yyyyMMddHHmmss"
$distpath = '.\dist\windows\tao_win_0.1.0_build' + $date

pyinstaller --onefile `
	--log-level=WARN `
	--workpath .build `
	--distpath $distpath `
	--noconfirm `
	tao.spec

deactivate
