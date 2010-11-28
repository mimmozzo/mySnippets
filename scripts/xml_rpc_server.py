#!/usr/bin/env python

import os
import SimpleXMLRPCServer

def ls(directory):
	try:
		return os.listdir(directory)
	except OSError:
		return []

def cb(obj):
	print "OBJECT::", obj
	print "OBJECT.__class__::", obj.__class__
	return obj.cb()

def main():
	s = SimpleXMLRPCServer.SimpleXMLRPCServer(('127.0.0.1',10005))
	s.register_function(ls)
	s.register_function(cb)
	s.serve_forever()

if __name__ == "__main__":
	main()
