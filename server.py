#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os.path
import os

METODOS_ACEPTADOS = ["INVITE","BYE","ACK"]

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            # Lee linea a lina lo que llega del cliente
          
            line = self.rfile.read()
            print "Recibo del cliente"
            print line
            #Comprobamos si hay linea en blanco
            if not line:
                break
            sip = "SIP/2.0\r\n\r\n"
            #miro aqui el codigo 400 xq el split me corta los \r\n
            if 'sip:' not in line or sip not in line or "@" not in line: #volver a mirar esto bien,incluir@!!!!!!!!!!!!!!!!
                self.wfile.write("SIP/2.0 400 Bad Request\r\n\r\n")
                sys.exit()
            #troceamos la linea que nos llega
            line = line.split()
            
            #line[1] = line[1].split(":")
            print "LINEA TROCEADA"
            print line
            
            if line[0] == "INVITE":
                trying = "SIP/2.0 100 Trying\r\n\r\n"
                ring = "SIP/2.0 180 Ring\r\n\r\n"
                ok = "SIP/2.0 200 OK\r\n\r\n"
                cod_respuesta = trying + ring + ok
                self.wfile.write(cod_respuesta)
            if line[0] not in METODOS_ACEPTADOS:
                self.wfile.write("SIP/2.0 405 Method Not Allowed\r\n\r\n")
            
            if line[0] == "ACK":
                print "me llega ACK,envio RTP"
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 <' + FICHERO_AUDIO
                os.system(aEjecutar)
            if line[0] == "BYE":    
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
   
    if len(sys.argv) != 4 or os.path.exists(sys.argv[3]) == False:
        print "Usage : python server.py IP port audio_file"
        sys.exit()
 
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    FICHERO_AUDIO = sys.argv[3]
    
  
   
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", PORT), EchoHandler)
    print "Listening..."
    serv.serve_forever()
