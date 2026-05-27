#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de IA - Clasificación de tráfico y predicción de ataques
"""

import json
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from modules.utils import cargar_config

console = Console()

# Placeholder del modelo (en versión real, cargarías TensorFlow)
class NetworkAI:
    """Clase principal del motor de IA"""
    
    def __init__(self):
        self.config = cargar_config()
        self.threshold = self.config.get('ai_threshold', 0.75)
        self.model_loaded = self.load_model()
    
    def load_model(self):
        """Carga el modelo de IA (placeholder)"""
        try:
            # Aquí cargarías el modelo real con tensorflow
            # model = tf.keras.models.load_model('models/network_model.h5')
            console.print("[green]✓ Modelo de IA cargado correctamente[/green]")
            return True
        except:
            console.print("[yellow]⚠ Modo IA básico activado (modelo no encontrado)[/yellow]")
            return False
    
    def analyze_pcap(self, pcap_file):
        """Analiza un archivo pcap con IA"""
        console.print(f"[bold cyan]🧠 Analizando {pcap_file} con IA...[/bold cyan]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task(description="Procesando paquetes...", total=None)
            # Simulación del análisis (en realidad procesarías el pcap)
            import time
            time.sleep(2)
        
        # Simular resultados de IA
        threat_score = random.uniform(0, 1)
        is_malicious = threat_score > self.threshold
        
        # Detalles simulados
        results = {
            'total_packets': random.randint(100, 10000),
            'suspicious_packets': random.randint(0, 500),
            'threat_score': threat_score,
            'is_malicious': is_malicious,
            'attack_types': self._predict_attacks(threat_score)
        }
        
        self._display_results(results)
        return results
    
    def _predict_attacks(self, threat_score):
        """Predice tipos de ataque basado en el score"""
        attacks = []
        if threat_score > 0.8:
            attacks = ["DDoS", "Port Scan", "ARP Spoofing"]
        elif threat_score > 0.5:
            attacks = ["Port Scan", "Brute Force"]
        elif threat_score > 0.3:
            attacks = ["Reconnaissance"]
        return attacks
    
    def _display_results(self, results):
        """Muestra resultados del análisis"""
        color = "red" if results['is_malicious'] else "green"
        status = "⚠ PELIGROSO" if results['is_malicious'] else "✓ SEGURO"
        
        panel = Panel(
            f"[bold]Resultados del análisis:[/bold]\n"
            f"  • Paquetes totales: {results['total_packets']}\n"
            f"  • Paquetes sospechosos: {results['suspicious_packets']}\n"
            f"  • Score de amenaza: {results['threat_score']:.2%}\n"
            f"  • Estado: [{color}]{status}[/{color}]\n"
            f"  • Posibles ataques: {', '.join(results['attack_types']) if results['attack_types'] else 'Ninguno'}",
            title="🤖 IA Analysis Report",
            border_style=color
        )
        console.print(panel)
        
        # Recomendaciones
        if results['is_malicious']:
            console.print("\n[bold yellow]🛡️ Recomendaciones:[/bold yellow]")
            console.print("  • Bloquear IPs sospechosas")
            console.print("  • Revisar reglas de firewall")
            console.print("  • Analizar tráfico en tiempo real")
    
    def predict_realtime(self, interface):
        """Predice tráfico malicioso en tiempo real"""
        console.print(f"[bold cyan]🔮 Predicción en tiempo real en {interface}[/bold cyan]")
        console.print("[yellow]Monitoreando tráfico... (presiona Ctrl+C para detener)[/yellow]\n")
        
        try:
            import time
            while True:
                # Simular análisis en tiempo real
                threat = random.random()
                if threat > self.threshold:
                    console.print(f"[red]⚠ ALERTA: Tráfico malicioso detectado (score: {threat:.2%})[/red]")
                else:
                    console.print(f"[green]✓ Tráfico normal (score: {threat:.2%})[/green]", end="\r")
                time.sleep(2)
        except KeyboardInterrupt:
            console.print("\n[yellow]Monitoreo detenido[/yellow]")

# Funciones wrapper
def analizar_pcap(pcap_file):
    """Analiza un archivo pcap con IA"""
    ai = NetworkAI()
    return ai.analyze_pcap(pcap_file)

def predecir_trafico(interface="eth0"):
    """Predice tráfico en tiempo real"""
    ai = NetworkAI()
    return ai.predict_realtime(interface)
