import os, socket, sys

MAXBYTES = 4096

if len(sys.argv) != 3:
	print('Usage:', sys.argv[0], 'hote port')
	sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
af, socktype, proto, canonname, sockaddr = socket.getaddrinfo(HOST, PORT)[0]
# get protocol informations of server (list of accepted protocols)
print("Layer 3 (network) protocol:", af) # IPv4 or IPv6
print("Layer 4 (transport) protocol:", socktype) # TCP or UDP
s = socket.socket(af, socket.SOCK_STREAM) # create same type of socket as server
s.connect(sockaddr)
print('connected to:', sockaddr)
while True: # Client synchrone !! On alterne écriture vers serveur
# et lecture depuis serveur. Le serveur doit donc lui aussi alterner
	line = os.read(0, MAXBYTES)
	if len(line) == 0:
		s.shutdown(socket.SHUT_WR)
		break
	s.send(line)
	data = s.recv(MAXBYTES)
	if len(data) == 0:
		break
	os.write(1, data)
s.close()