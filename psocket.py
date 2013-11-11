import socket
import threading
import time
import os

HOST=''
PORT='8111'

class PSocket(socket.SocketType): 
  def __init__(self, host, port): 
    print "Constructor called"
    socket.SocketType.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
    self.host = host
    self.port = port
    try: 
      self.bind((self.host,self.port))
    except:  
      print "Unable to open socket!"
    try: 
      self.listen(2000)
    except:
      print "Unable to listen on %s:%d", self.host,self.port 
    try: 
      c_connObj, c_connAddr = self.accept()
    except:
      print "unable to accept connections!"
      



#webby = PSocket('127.0.0.1', 8111)


