#!/usr/bin/env python

def print_package_imports():
	
	# lettura file e separazione token di interesse completata, manca 
	# la costruzione del set dei package e l'abbinamento con una lista di import.

	import_list_file = None
	
	try:
		import_list_file = open("lista_import",'r')
		print "file aperto: " + str(import_list_file)
		for line in import_list_file:
			#print line
			#print line.rpartition("/")
			path,sep,file_and_import = line.rpartition("/")
			#print path
			java_file,sep,pkg_import = file_and_import.rpartition(":import ")
			print pkg_import

	except EnvironmentError:
		print "Cannot open file"
	finally:
		if import_list_file is not None:
			import_list_file.close()

def main():
	print_package_imports()

if __name__ == "__main__":
	main()
