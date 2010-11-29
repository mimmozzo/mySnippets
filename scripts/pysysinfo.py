#!/usr/bin/env python
# A sysinfo script
import subprocess

# funzione uname
def uname_func():
	
	uname = "uname"
	uname_arg = "-a"
	print "Gathering information with %s command\n" % uname
	subprocess.call([uname,uname_arg])
	print "\n"

# funzione df
def df_func():
	
	df = "df"
	df_arg = "-h"
	print "Gathering information with %s command\n" % df
	subprocess.call([df,df_arg])
	print "\n"

# il main chiama le altre funzioni
def main():

	uname_func()
	df_func()

if __name__ == "__main__":
	main()
