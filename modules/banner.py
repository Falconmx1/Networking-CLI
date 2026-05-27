#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo del banner - Estilo cyberpunk con efectos
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def mostrar_banner():
    """Muestra el banner principal de Networking-CLI"""
    
    banner_ascii = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███▄    █  ██▓▓█████  ▄▄▄     █    ██▒    ██▓             ║
║   ██ ▀█   █ ▓██▒▓█   ▀ ▒████▄   ██  ▓██▒   ▓██▒             ║
║  ▓██  ▀█ ██▒▒██▒▒███   ▒██  ▀█▄ ▓██  ▒██░   ▒██░             ║
║  ▓██▒  ▐▌██▒░██░▒▓█  ▄ ░██▄▄▄▄██▓▓█  ░██░   ▒██░             ║
║  ▒██░   ▓██░░██░░▒████▒ ▓█   ▓██▒▒▒██████▓▒  ░██████▒        ║
║  ░ ▒░   ▒ ▒ ░▓  ░░ ▒░ ░ ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ░ ▒░▓  ░        ║
║  ░ ░░   ░ ▒░ ▒ ░ ░ ░  ░  ▒   ▒▒ ░░░▒░ ░ ░   ░ ░ ▒  ░        ║
║     ░   ░ ░  ▒ ░   ░     ░   ▒    ░░░ ░ ░     ░ ░           ║
║           ░  ░     ░  ░      ░  ░   ░           ░  ░        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    
    # Texto con gradiente de colores
    titulo = Text("Networking-CLI v1.0", style="bold cyan")
    subtitulo = Text("IA Powered Network Toolkit", style="yellow italic")
    eslogan = Text("\"El admin de tu red con superpoderes\"", style="green bold")
    
    # Panel principal
    panel = Panel(
        f"{banner_ascii}\n"
        f"                    {titulo}\n"
        f"                    {subtitulo}\n"
        f"                    {eslogan}\n"
        f"\n[dim]⚠️  Uso ético y legal solamente. El autor no se responsabiliza por mal uso.[/dim]",
        border_style="cyan",
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()  # Línea vacía después del banner

def mostrar_progreso(actual, total, mensaje="Procesando"):
    """Muestra una barra de progreso estilo hacker"""
    porcentaje = int((actual / total) * 100)
    barra_largo = 40
    lleno = int(barra_largo * actual / total)
    barra = "█" * lleno + "░" * (barra_largo - lleno)
    
    console.print(f"\r[cyan]{mensaje}:[/cyan] [{barra}] {porcentaje}%", end="")
    if actual == total:
        console.print()
