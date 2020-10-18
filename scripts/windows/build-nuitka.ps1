./.env/scripts/activate.ps1

python -m nuitka `
    --follow-imports `
    --recurse-all `
    --plugin-enable="pylint-warnings" `
    --mingw64 `
    .\src\tao.py

deactivate
