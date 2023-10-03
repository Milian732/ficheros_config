#!/usr/bin/python3


import sys
import netifaces
import json

lista_interfaces = netifaces.interfaces()

for interfaz in lista_interfaces:

    datos_interfaz = netifaces.ifaddresses(interfaz)
    
    if netifaces.AF_INET in datos_interfaz:
        ipv4 = datos_interfaz[netifaces.AF_INET]
        for ip in ipv4:
            print(f"La direccion IP de {interfaz} es: {ip['addr']}")
    
    

sys.exit(0)
