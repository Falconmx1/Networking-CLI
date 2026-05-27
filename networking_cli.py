#!/usr/bin/env python3
# Este es el main, el que orquesta toda la sinfonía.

import argparse
from rich.console import Console
from rich.table import Table
from modules.banner import mostrar_banner
from modules.scanner import escanear_puertos
from modules.sniffer import iniciar_sniffer
from modules.ai_engine import analizar_con_ia

console = Console()

def main():
    mostrar_banner()
    parser = argparse.ArgumentParser(description="Networking-CLI - Herramienta de IA para pentesting")
    parser.add_argument("--scan", help="Escanea una red (ej: 192.168.1.0/24)")
    parser.add_argument("--sniff", action="store_true", help="Inicia sniffer de paquetes")
    parser.add_argument("--interface", default="eth0", help="Interfaz de red para sniffing")
    parser.add_argument("--ai-analyze", help="Analiza un archivo .pcap con IA")
    args = parser.parse_args()

    if args.scan:
        escanear_puertos(args.scan)
    elif args.sniff:
        iniciar_sniffer(args.interface)
    elif args.ai_analyze:
        analizar_con_ia(args.ai_analyze)
    else:
        console.print("[bold yellow]Usa --help para ver las opciones criminales[/bold yellow]")

if __name__ == "__main__":
    main()
