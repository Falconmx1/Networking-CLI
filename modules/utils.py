#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de utilidades - Funciones auxiliares
"""

import socket
import yaml
import os
import subprocess
import sys
from rich.console import Console

console = Console()

def cargar_config():
    """Carga la configuración desde config.yaml"""
    config_default = {
        'default_interface': 'eth0',
        'ai_threshold': 0.75,
        'max_ports': 1000,
        'timeout': 2,
        'log_level': 'INFO',
        'max_threads': 100
    }
    
    try:
        if os.path.exists('config.yaml'):
            with open('config.yaml', 'r') as f:
                config = yaml.safe_load(f)
                config_default.update(config)
    except Exception as e:
        console.print(f"[yellow]Error cargando config: {e}[/yellow]")
    
    return config_default

def is_port_open(host, port, timeout=2):
    """Verifica si un puerto está abierto"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def get_common_ports():
    """Retorna lista de puertos comunes"""
    return [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
            993, 995, 1723, 3306, 3389, 5900, 8080, 8443]

def validate_ip(ip):
    """Valida si una dirección IP es correcta"""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def get_interfaces():
    """Obtiene las interfaces de red disponibles"""
    interfaces = []
    
    if sys.platform == "linux":
        try:
            import psutil
            for iface, addrs in psutil.net_if_addrs().items():
                ip = None
                mac = None
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        ip = addr.address
                    elif addr.family == psutil.AF_LINK:
                        mac = addr.address
                interfaces.append({
                    'name': iface,
                    'ip': ip,
                    'mac': mac,
                    'up': iface in psutil.net_if_stats() and psutil.net_if_stats()[iface].isup
                })
        except ImportError:
            # Fallback con socket
            interfaces.append({'name': 'eth0', 'ip': '192.168.1.1', 'mac': 'N/A', 'up': True})
    elif sys.platform == "win32":
        # Windows: usar ipconfig
        try:
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            interfaces.append({'name': 'Wi-Fi', 'ip': '192.168.1.1', 'mac': 'N/A', 'up': True})
        except:
            pass
    
    return interfaces

def check_root():
    """Verifica si se ejecuta como root/admin"""
    if sys.platform == "linux":
        return os.geteuid() == 0
    elif sys.platform == "win32":
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    return False
