#!/usr/bin/python3

import sys
import os

f = open("/etc/passwd","r")

for linea in f:

    uid = int(linea.split(":")[2])
    if uid > 1000:
        personal = linea.split(":")[5]
        usuario = linea.split(":")[0]
        if os.path.isdir(personal):
            print("la carpeta del usuario "+str(usuario)+" con uid "+str(uid)+" existe y su directorio es "+str(personal))
        else:
            print("la carpeta no existe")
        
f.close()
