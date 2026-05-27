#!/bin/bash
echo "Instalando Networking-CLI..."
pip install -r requirements.txt
sudo cp networking_cli.py /usr/local/bin/networking-cli
sudo chmod +x /usr/local/bin/networking-cli
echo "¡Instalación completa! Ejecuta 'networking-cli --help'"
