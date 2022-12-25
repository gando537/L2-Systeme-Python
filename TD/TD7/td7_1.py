import socket


HOST = '127.0.0.1' # or 'localhost' or '' - Standard loopback interface address
PORT = 2000 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket: # AF_INET: IPv4
# SOCK_STREAM: TCP
	socket_add = ('',PORT)
	serversocket.bind(socket_add) # bind this socket to specific port on host
	serversocket.listen() # make the socket a listening one
	
	while True:
		clientsocket, (addr, port) = serversocket.accept() # blocking. returns if a client connects.	
		with clientsocket:
			print('Connected by application: %d on machine: %s' % (port, addr))
			data = clientsocket.recv(MAXBYTES)
			while len(data) > 0: # otherwise means a disconnection from the client side.
				clientsocket.sendall(data)
				data = clientsocket.recv(MAXBYTES)