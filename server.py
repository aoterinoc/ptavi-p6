#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os.path

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """
"""
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
"""
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
