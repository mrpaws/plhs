#!/usr/bin/python -tt
## paws' lightweight http server 
## 
## milestones: 	- threaded connection acceptance model
## 		- 

import sys
import socket
import threading
import time



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8111              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
