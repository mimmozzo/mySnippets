#!/usr/bin/env python

def print_class_methods():
	
	# lettura file e separazione token di interesse completata, manca 
	# la costruzione del set dei package e l'abbinamento con una lista di method.

	method_list_file = None
	
	try:
		method_list_file = open("lista_method",'r')
		print "file aperto: " + str(method_list_file)
		for line in method_list_file:
			#print line
			#print line.rpartition("/")
			path,sep,file_and_method = line.rpartition("/")
			#print path
			java_file,sep,pkg_method = file_and_method.rpartition(":method ")
			print pkg_method

	except EnvironmentError:
		print "Cannot open file"
	finally:
		if method_list_file is not None:
			method_list_file.close()

def main():
	print_class_methods()

if __name__ == "__main__":
	main()
