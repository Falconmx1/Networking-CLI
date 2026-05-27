#!/usr/bin/env python3
# networking_cli.py - Punto de entrada principal

import argparse
from banner import mostrar_banner
from scanner import escanear_puertos
from sniffer import iniciar_sniffer

def main():
    mostrar_banner()
    parser = argparse.ArgumentParser(description="Networking-CLI - IA para pentesting")
    parser.add_argument("--scan", help="Escanea una red (ej: 192.168.1.0/24)")
    parser.add_argument("--sniff", action="store_true", help="Inicia sniffer de paquetes")
    parser.add_argument("--interface", help="Interfaz de red para sniffing")
    args = parser.parse_args()

    if args.scan:
        escanear_puertos(args.scan)
    elif args.sniff:
        iniciar_sniffer(args.interface)
    else:
        print("Usa --help para ver opciones")

if __name__ == "__main__":
    main()
