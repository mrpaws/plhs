import socket
import threading
import time
import os

HOST=''
PORT='8111'

class PServer(socket.SocketType): 
  def __init__(self, host, port): 
    socket.SocketType.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
    self.host = host
    self.port = port
    self.data = ''
    try: 
      self.bind((self.host,self.port))
    except:  
      print "Unable to open socket!"
    try: 
      self.listen(2000)
    except:
      print "Unable to listen on %s:%d" % self.host, self.port 
    while True: 
      try:
        c_connObj, c_connAddr = self.accept()
      except: 
        print "ERROR: Connection attempt failed from %s" % str(c_connAddr)
      print "Received connection from", c_connAddr
      try: 
        data = c_connObj.recv(75000)
      except:
        print "ERROR: Failed to receive from %s" % str(c_connAddr)
      print "Received data from client (%s)" % str(c_connAddr)
      if not data: 
        break
      try:
        c_connObj.sendall(data)
      except:
        print "ERROR: Failed to send data to %s" % str(c_connAddr)
      print "Sent response to client %s" % str(c_connAddr) 
      try:
        c_connObj.close()
      except:
        print "ERROR: Unable to close connection with (%s)!" % str(c_connAddr)  
      print "Connection closed with %s" %  str(c_connAddr)

	
      



#webby = PServer('127.0.0.1', 8111)


