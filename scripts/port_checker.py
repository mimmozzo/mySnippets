#!/usr/bin/env python
import socket
import re
import sys

"""
Questo metodo tenta di instaurare una connessione tcp address:port
ritorna True se la destinazione e' raggiungibile, False altrimenti.
"""

def check_server (address, port):
	
	#print "Attempt to connect to %s, port %d\n" % (address, port)
	try:	
		s = socket.create_connection((address,port),timeout=0.15)
		#print "Connected to address %s, port %s" % (address,port)
		return True
	except socket.error, e:
		#print "Connection to address %s, port %s failed: %s\n" % (address, port, e)
		return False

def main():
	check_server("localhost",5432)


if __name__ == "__main__":
	main()
