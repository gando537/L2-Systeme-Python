import os, select, socket, sys
HOST = '127.0.0.1' # or 'localhost' or '' - Standard loopback interface address
PORT = 2005 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()
nb_open = 0
# Create list of potential active sockets and place serversocket in
# first position
socketlist = [serversocket]
first = True
while first or nb_open > 0:
	first = False
	activesockets, _, _ = select.select(socketlist, [], [])
	for s in activesockets:
		if s == serversocket:
			clientsocket, (addr, port) = serversocket.accept()
			socketlist.append(clientsocket)
			print("Incoming connection from %s on port %d..." % (addr, port))
			nb_open += 1
		else:
			msg = s.recv(MAXBYTES)
			msg_decod = msg.decode('utf-8')
			cmd = msg_decod.split()
			comde = cmd[0]
			argument = [cmd[1:]]
			tupl_cmd = (comde,cmd)
			list_cmd = []
			list_cmd.append(tupl_cmd)
			cmmd , arg = list_cmd[0]
			if len(msg) == 0:
				print("NULL message. Closing connection...")
				s.close()
				socketlist.remove(s)
				nb_open -= 1
			else:
				os.dup2(s.fileno(),1)
				os.dup2(s.fileno(),2) 
				if os.fork() == 0:
					serversocket.sendall(os.execvp(cmmd,arg))
					
serversocket.close()
print("Last connection closed. Bye!")
sys.exit(0)