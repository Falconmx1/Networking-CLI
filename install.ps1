Write-Host "Instalando Networking-CLI..." -ForegroundColor Cyan
pip install -r requirements.txt
Copy-Item networking_cli.py C:\Windows\System32\networking-cli.py
Write-Host "¡Listo! Ejecuta 'python C:\Windows\System32\networking-cli.py --help'"
