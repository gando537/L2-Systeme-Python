import os,sys

# le programme générique client-server

# les deux modules suivants doivent être écrits
# ils sont supposés fournir les deux méthodes:
# client.client()
# server.server()

import client,server

if __name__ == '__main__':

	rfd1, wfd1 = os.pipe()			# tube père vers fils
	rfd2, wfd2 = os.pipe()			# tube fils vers père
	childpid = os.fork()
	if childpid == 0: 				# child
		os.close(wfd1)
		os.close(rfd2)
		server.server(rfd1,wfd2)
	else :							# père
		os.close(rfd1)
		os.close(wfd2)
		client.client(rfd2,wfd1)	# père exécute client
		os.waitpid(childpid, 0)		# attendre fin fils
	sys.exit(0)

