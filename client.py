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

LINE = METODO.upper() + " sip:" + RECEPTOR+ "@" + SERVER + " SIP/2.0\r\n"
print LINE
print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')

#Excepcion en caso de establecer conexion con un puerto no abierto
try:
    data = my_socket.recv(1024)
    print 'Recibido -- '
    print data
   
    if data == 'SIP/2.0 400 Bad Request\r\n\r\n':
        sys.exit()  #ESTO ESTA BIEN ASI???
    trying = "SIP/2.0 100 Trying\r\n\r\n"
    ring = "SIP/2.0 180 Ring\r\n\r\n"
    ok = "SIP/2.0 200 OK\r\n\r\n"
    respuesta = trying + ring + ok
    if data == respuesta:
        print "He recibido las respuestas 100,180,200 mando ACK"
        asentimiento = "ACK" + " sip:" + RECEPTOR+ "@" + SERVER + " SIP/2.0\r\n\r\n"
        print "Enviando: " + asentimiento
        my_socket.send(asentimiento)

except (socket.error):
    print "No server listening at " + str(SERVER) + " port " + str(PORT)
    sys.exit()

print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
