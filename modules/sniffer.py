#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo sniffer - Captura de paquetes en tiempo real
"""

import sys
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from modules.utils import cargar_config

console = Console()

# Intentar importar scapy (solo si está instalado)
try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False
    console.print("[red]⚠ Scapy no está instalado. Ejecuta: pip install scapy[/red]")

class PacketSniffer:
    """Clase principal del sniffer"""
    
    def __init__(self, interface, packet_count=50):
        self.interface = interface
        self.packet_count = packet_count
        self.packets = []
        
    def packet_callback(self, packet):
        """Callback que se ejecuta por cada paquete capturado"""
        self.packets.append(packet)
        self.show_packet(packet)
        
        if len(self.packets) >= self.packet_count:
            return True  # Detener sniffing
    
    def show_packet(self, packet):
        """Muestra información del paquete en tiempo real"""
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            proto = "?"
            
            if TCP in packet:
                proto = f"TCP:{packet[TCP].sport}→{packet[TCP].dport}"
                color = "green"
            elif UDP in packet:
                proto = f"UDP:{packet[UDP].sport}→{packet[UDP].dport}"
                color = "yellow"
            elif ICMP in packet:
                proto = "ICMP"
                color = "magenta"
            else:
                proto = "IP"
                color = "blue"
            
            console.print(f"[{color}]📦 {src} → {dst} | {proto}[/{color}]")
    
    def start(self):
        """Inicia la captura de paquetes"""
        if not SCAPY_AVAILABLE:
            console.print("[red]No se puede iniciar sniffer sin Scapy[/red]")
            return
        
        console.print(f"[bold cyan]👃 Iniciando sniffer en {self.interface}[/bold cyan]")
        console.print(f"[yellow]Capturando {self.packet_count} paquetes...[/yellow]")
        console.print("[dim]Presiona Ctrl+C para detener[/dim]\n")
        
        try:
            sniff(
                iface=self.interface,
                prn=self.packet_callback,
                count=self.packet_count,
                store=False
            )
            self.show_summary()
        except KeyboardInterrupt:
            console.print("\n[yellow]⚠ Sniffer detenido por el usuario[/yellow]")
            self.show_summary()
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
    
    def show_summary(self):
        """Muestra resumen de la captura"""
        if not self.packets:
            console.print("[yellow]No se capturaron paquetes[/yellow]")
            return
        
        # Contar por protocolo
        stats = {"TCP": 0, "UDP": 0, "ICMP": 0, "OTHER": 0}
        for p in self.packets:
            if TCP in p:
                stats["TCP"] += 1
            elif UDP in p:
                stats["UDP"] += 1
            elif ICMP in p:
                stats["ICMP"] += 1
            else:
                stats["OTHER"] += 1
        
        table = Table(title="📊 Resumen de captura", style="cyan")
        table.add_column("Protocolo", style="green")
        table.add_column("Paquetes", style="yellow")
        table.add_column("%", style="white")
        
        total = len(self.packets)
        for proto, count in stats.items():
            if count > 0:
                percentage = (count / total) * 100
                table.add_row(proto, str(count), f"{percentage:.1f}%")
        
        console.print(table)
        console.print(f"\n[bold green]✓ Total paquetes capturados: {total}[/bold green]")

def iniciar_sniffer(interface="eth0", packet_count=50):
    """Función wrapper para iniciar el sniffer"""
    sniffer = PacketSniffer(interface, packet_count)
    sniffer.start()
