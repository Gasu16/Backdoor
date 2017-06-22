#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from thread import *
import time
import SocketServer
import os
import subprocess
import shlex

HOST = ''  # localhost
PORT = 8888  # Porta da usare

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creata")

# Collega la socket alla porta e all'host locale
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Collegamento fallito. Error Code : " + str(msg[0]) + " - Message: " + msg[1])
    sys.exit()

time.sleep(1)
print("Collegamento alla socket...")
time.sleep(1)
print("Collegato")

# Ascoltiamo la socket
s.listen(10)
print("Socket in ascolto")

comandi = {"mostra", "elimina"}
#utenti = {}  # Dizionario con coppia Host: IP
i = -1  # Perche' quando andiamo ad aggiungere il primo utente esso sara' il numero 0
        #  quindi i va a 0 alla prima aggiunta per questo partiamo da -1
IP_Utenti = [] # Lista degli IP degli utenti connessi al server


def invia_dati(conn):
    global i
    path = "/home/matteo"
    while True:
		conn.send("Inserisci comando: ")
		dati = conn.recv(1024)  # il server riceve 1 kB per volta
		var_ip = conn.getpeername() # Leggere da qui l'IP di chi manda i dati al server
		if (dati.strip() == "exit"): # Si usa il metodo strip() perche' la stringa dati contiene anche l'invio \n
			indice = IP_Utenti.index(var_ip)
			del IP_Utenti[indice]
			print("Numero utenti connessi lista: " + str(len(IP_Utenti)))
			print("IP utenti connessi: " + str(IP_Utenti))
			i = indice
			i -= 1
			break
			#print(i)
		elif (dati.strip() == "mostra"):
			subprocess.call(["ls"])
            #args = shlex.split(dati)
            #print(args)
            #p = subprocess.Popen(args)
            #print(p)
            #todel = input("Quale cartella vuoi eliminare...: ")
            #print("execpath: " + os.get_exec_path())
            #print(os.listdir(path))            
            #pro = subprocess.Popen(shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            #print(pro)
            #os.rmdir("/home/matteo/Scrivania/REM")
		elif (dati.strip() == "help"):
			print("pwd, ps, goto, mostra")
		elif (dati.strip() == "pwd"):
			subprocess.call(["pwd"])
		elif (dati.strip() == "ps"):
			subprocess.call(["ps"])
		elif (dati.strip() == "goto"):
		#	go = raw_input("Cartella dove andare: ")
			subprocess.call(["cd " + go])
			print("Siamo ora in: " + subprocess.call(["pwd"]))
		elif (dati.strip() == "shell"):
			if len(dati.strip()) > 1:
				proc2 = subprocess.Popen(dati.strip(), shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE)
				output = proc2.stdout.read() + proc2.stderr.read()
			else:
				output = 'args must follow "shell"'
		print("Inviato da:  " + str(var_ip) + " - " + dati)
    conn.close()


# manteniamo il collegamento col client
while 1:
    # ci connettiamo...
    conn, addr = s.accept() # CAUSA DEL BUG
    #utenti.append(addr[0])
    #utenti[addr] = conn
    var_ip = conn.getpeername()
    IP_Utenti.append(var_ip)
    i += 1
    print(i)
    print("\n")
    print("Connesso con " + addr[0] + ":" + str(addr[1]))

    print("Numero utenti connessi lista: " + str(len(IP_Utenti)))
    print("IP utenti connessi: " + str(IP_Utenti))
    start_new_thread(invia_dati, (conn,))
s.close()
