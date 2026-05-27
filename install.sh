#!/bin/bash
echo "[+] Instalando Networking-CLI para Linux..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo cp networking_cli.py /usr/local/bin/networking-cli
sudo chmod +x /usr/local/bin/networking-cli
echo "[✓] Listo, papá. Ejecuta 'networking-cli --help' para empezar."
