#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de escaneo de puertos con optimización por IA
"""

import socket
import threading
import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from modules.utils import is_port_open, get_common_ports, cargar_config

console = Console()

class Scanner:
    """Clase principal de escaneo"""
    
    def __init__(self, target, ports_range="1-1000"):
        self.target = target
        self.ports_range = ports_range
        self.open_ports = []
        self.lock = threading.Lock()
        self.config = cargar_config()
        
    def parse_ports(self):
        """Parsea el rango de puertos"""
        if '-' in self.ports_range:
            start, end = map(int, self.ports_range.split('-'))
            return range(start, end + 1)
        elif ',' in self.ports_range:
            return [int(p.strip()) for p in self.ports_range.split(',')]
        else:
            return [int(self.ports_range)]
    
    def scan_port(self, port):
        """Escanea un puerto individual"""
        if is_port_open(self.target, port, timeout=self.config.get('timeout', 2)):
            with self.lock:
                self.open_ports.append(port)
                # Mostrar en tiempo real
                console.print(f"[green]✓ Puerto {port} ABIERTO[/green]")
    
    def run(self):
        """Ejecuta el escaneo con optimización IA"""
        ports = self.parse_ports()
        total_ports = len(ports) if isinstance(ports, list) else len(list(ports))
        
        console.print(f"[bold cyan]🎯 Escaneando objetivo: {self.target}[/bold cyan]")
        console.print(f"[yellow]📡 Puertos a escanear: {total_ports}[/yellow]")
        
        # Si hay muchos puertos, sugerir modo IA
        if total_ports > 1000:
            console.print("[blue]🧠 Usando modo IA: escaneando solo puertos comunes primero...[/blue]")
            common = get_common_ports()
            ports = common + [p for p in ports if p not in common][:500]
        
        # Escaneo con threads
        threads = []
        max_threads = self.config.get('max_threads', 100)
        
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Escaneando...", total=total_ports)
            
            for port in ports:
                t = threading.Thread(target=self.scan_port, args=(port,))
                threads.append(t)
                t.start()
                progress.advance(task)
                
                # Control de threads
                if len(threads) >= max_threads:
                    for thread in threads:
                        thread.join()
                    threads = []
            
            # Esperar threads restantes
            for t in threads:
                t.join()
        
        # Mostrar resultados
        self.show_results()
    
    def show_results(self):
        """Muestra resultados en tabla bonita"""
        if not self.open_ports:
            console.print("[yellow]⚠ No se encontraron puertos abiertos[/yellow]")
            return
        
        table = Table(title=f"📊 Resultados para {self.target}", style="cyan")
        table.add_column("Puerto", style="green", justify="center")
        table.add_column("Estado", style="white", justify="center")
        table.add_column("Servicio", style="yellow")
        
        for port in sorted(self.open_ports):
            try:
                service = socket.getservbyport(port)
            except:
                service = "desconocido"
            table.add_row(str(port), "✅ ABIERTO", service)
        
        console.print(table)
        console.print(f"\n[bold green]✓ Escaneo completado. Puertos abiertos: {len(self.open_ports)}[/bold green]")

def escanear_puertos(target, ports_range="1-1000"):
    """Función wrapper para escanear puertos"""
    scanner = Scanner(target, ports_range)
    scanner.run()
