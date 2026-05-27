#!/bin/bash
# Networking-CLI Installer for Linux

set -e  # Salir si hay error

echo "========================================="
echo "  Networking-CLI Installer v1.0"
echo "  AI-Powered Network Toolkit"
echo "========================================="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 no encontrado. Instálalo primero."
    exit 1
fi

echo "[✓] Python 3 encontrado"

# Crear entorno virtual
echo "[+] Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "[+] Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Crear directorios necesarios
mkdir -p logs

# Instalar comando global (opcional)
echo "[+] Instalando comando 'networking-cli'..."
sudo cp networking_cli.py /usr/local/bin/networking-cli
sudo chmod +x /usr/local/bin/networking-cli

echo ""
echo "========================================="
echo "  ✓ Instalación completada"
echo "========================================="
echo ""
echo "Ejecuta: networking-cli --help"
echo "O usa: python3 networking_cli.py --help"
echo ""
