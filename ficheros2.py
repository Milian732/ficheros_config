#!/usr/bin/python3

import sys
import os

f1 = open("/etc/passwd","r")

for linea in f1:

    login = linea.split(":")[0] 
    shell = linea.split(":")[6].strip()
    if shell == "/bin/bash":
        f2 = open("/etc/shadow","r")

        for linea in f2:

            usuario = linea.split(":")[0]
            contraseña = linea.split(":")[1]
            if contraseña != "!" and contraseña != "*" and contraseña != "!*":
                if login == usuario:
                    print(usuario,contraseña)

        f2.close()
f1.close()

sys.exit(0)
