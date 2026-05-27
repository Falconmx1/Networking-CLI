# Networking-CLI Installer for Windows PowerShell
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Networking-CLI Installer v1.0" -ForegroundColor Green
Write-Host "  AI-Powered Network Toolkit" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python no encontrado. Instálalo desde python.org" -ForegroundColor Red
    exit 1
}

# Crear entorno virtual
Write-Host "[+] Creando entorno virtual..." -ForegroundColor Cyan
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "[+] Instalando dependencias..." -ForegroundColor Cyan
pip install --upgrade pip
pip install -r requirements.txt

# Crear directorios
New-Item -ItemType Directory -Force -Path logs | Out-Null

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  ✓ Instalación completada" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecuta: python networking_cli.py --help" -ForegroundColor Yellow
Write-Host ""
