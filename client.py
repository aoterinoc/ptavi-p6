#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

if len(sys.argv) != 3:
    print "Usage : python client.py method receiver@IP:SIPport"
    sys.exit()
METODO = sys.argv[1]
DATOS = sys.argv[2]

#Troceo argv[2] para obtener el server&port
DATOS = DATOS.split("@")
DATOS[1] = DATOS[1].split(":")
SERVER = DATOS[1][0]
PORT = int(DATOS[1][1])
RECEPTOR = DATOS[0]





# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

LINE = METODO.upper() + " sip:" + RECEPTOR+ "@" + SERVER + " SIP/2.0"
print LINE
print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')

#Excepcion en caso de establecer conexion con un puerto no abierto
try:
    data = my_socket.recv(1024)
    print 'Recibido -- ', data
except (socket.error):
    print "No server listening at " + str(SERVER) + " port " + str(PORT)
    sys.exit()

print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
