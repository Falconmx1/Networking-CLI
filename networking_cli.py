#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Networking-CLI - Herramienta de IA para pentesting y análisis de red
Uso ético y legal solamente.
"""

import argparse
import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
from modules.banner import mostrar_banner
from modules.scanner import escanear_puertos
from modules.sniffer import iniciar_sniffer
from modules.ai_engine import analizar_pcap, predecir_trafico
from modules.utils import check_root, validate_ip, get_interfaces

# Instalar rich traceback para errores bonitos
install()

console = Console()

def main():
    """Función principal que orquesta todo"""
    # Mostrar banner épico
    mostrar_banner()
    
    # Verificar permisos (opcional, solo si necesita root)
    # if not check_root():
    #     console.print("[yellow]⚠ Algunas funciones requieren permisos de administrador[/yellow]")
    
    parser = argparse.ArgumentParser(
        description="Networking-CLI - Herramienta de IA para pentesting y análisis de red",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s --scan 192.168.1.0/24
  %(prog)s --sniff --interface eth0 --packets 100
  %(prog)s --ai-analyze captura.pcap
  %(prog)s --interfaces
  %(prog)s --predict --interface wlan0
        """
    )
    
    # Argumentos principales
    parser.add_argument("--scan", "-s", type=str, help="Escanea una red (ej: 192.168.1.0/24 o 192.168.1.1)")
    parser.add_argument("--ports", "-p", type=str, default="1-1000", help="Rango de puertos (ej: 22,80,443 o 1-1000)")
    parser.add_argument("--sniff", action="store_true", help="Inicia sniffer de paquetes en tiempo real")
    parser.add_argument("--interface", "-i", type=str, default="eth0", help="Interfaz de red para sniffing")
    parser.add_argument("--packets", type=int, default=50, help="Número de paquetes a capturar (sniffer)")
    parser.add_argument("--ai-analyze", type=str, help="Analiza un archivo .pcap con IA")
    parser.add_argument("--predict", action="store_true", help="Predice tráfico malicioso en tiempo real")
    parser.add_argument("--interfaces", action="store_true", help="Lista las interfaces de red disponibles")
    parser.add_argument("--config", action="store_true", help="Muestra la configuración actual")
    parser.add_argument("--version", action="version", version="Networking-CLI v1.0.0")
    
    args = parser.parse_args()
    
    # Ejecutar según argumentos
    if args.interfaces:
        mostrar_interfaces()
    elif args.config:
        mostrar_config()
    elif args.scan:
        escanear_puertos(args.scan, args.ports)
    elif args.sniff:
        iniciar_sniffer(args.interface, args.packets)
    elif args.ai_analyze:
        analizar_pcap(args.ai_analyze)
    elif args.predict:
        predecir_trafico(args.interface)
    else:
        # Si no hay argumentos, mostrar ayuda con estilo
        console.print(Panel.fit(
            "[bold cyan]Networking-CLI v1.0 - IA Powered[/bold cyan]\n"
            "[yellow]Usa --help para ver los comandos disponibles[/yellow]\n\n"
            "[green]Ejemplos rápidos:[/green]\n"
            "  • Escaneo: [white]--scan 192.168.1.0/24[/white]\n"
            "  • Sniffer: [white]--sniff --interface wlan0[/white]\n"
            "  • IA: [white]--ai-analyze captura.pcap[/white]",
            title="🤖 Networking-CLI",
            border_style="cyan"
        ))

def mostrar_interfaces():
    """Muestra las interfaces de red disponibles"""
    interfaces = get_interfaces()
    if not interfaces:
        console.print("[red]No se encontraron interfaces de red[/red]")
        return
    
    table = Table(title="📡 Interfaces de Red Disponibles", style="cyan")
    table.add_column("Interfaz", style="green")
    table.add_column("IP", style="yellow")
    table.add_column("MAC", style="magenta")
    table.add_column("Status", style="white")
    
    for iface in interfaces:
        table.add_row(
            iface['name'],
            iface.get('ip', 'N/A'),
            iface.get('mac', 'N/A'),
            "🟢 Up" if iface.get('up') else "🔴 Down"
        )
    
    console.print(table)

def mostrar_config():
    """Muestra la configuración actual"""
    from modules.utils import cargar_config
    config = cargar_config()
    
    panel = Panel.fit(
        f"[bold]Configuración actual:[/bold]\n"
        f"  • Interfaz por defecto: {config.get('default_interface', 'eth0')}\n"
        f"  • Umbral de IA: {config.get('ai_threshold', 0.75)}\n"
        f"  • Máx puertos por scan: {config.get('max_ports', 1000)}\n"
        f"  • Timeout: {config.get('timeout', 2)}s\n"
        f"  • Log level: {config.get('log_level', 'INFO')}",
        title="⚙️ Configuration",
        border_style="green"
    )
    console.print(panel)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Interrupción detectada. Saliendo...[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error fatal: {e}[/red]")
        sys.exit(1)
