#!/usr/bin/env python
import sys
import port_checker

def port_scan(address):
	for i in range (1024):
		if port_checker.check_server(address,i):
			print "Port %d is open on address %s" % (i,address)

def main():
	address = sys.argv[1]
	print "Indirizzo per lo scan: " + address
	port_scan(address)

if __name__ == "__main__":
	main()
