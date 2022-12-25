import os, select, socket, sys, errno,signal

def capter_INT(sig_num, frame):
	mess = f"server connection closed in 10 s...".encode('utf-8')
	name = f"@server > ".encode('utf-8')
	print("\nconnection closed in 10s...")	
	for client_socket in clients:
		client_socket.send(name + mess)
	signal.alarm(10)

def capter_ALRM(sig_num, frame):
    print("Connection server closing")
    sys.exit(0)

HOST = '127.0.0.1' # or 'localhost' or '' - Standard loopback interface address
PORT = 2003 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 10000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
serversocket.bind((HOST, PORT))
serversocket.listen()

sockets_list = [serversocket,sys.stdin]
clients = {}

def _message(client_socket):
	try:
		message_header = client_socket.recv(MAXBYTES)
		if not len(message_header):
			return False
		return {"header": message_header, "data": client_socket.recv(MAXBYTES)}
	except :
		return False

pseudo_list = []
print("@server {} listening on port {}".format(HOST, PORT))
print("""
    \t -----------------------------------------------------------------------
    \t|\t              BIENVENUE !!!	                                |
    \t|\tQuelques commandes de bases :	                                |
    \t|\t- Pour envoyer un message à tout le monde : écrire et envoyer	|
    \t|\t- Pour quitter CTRL-C et le server fermera dans 10 secondes	|
    \t|\t- Pour bannir un client saisir : _@kick pseudo 		        |
    \t|\t  ex : _@kick gan2                                              |
    \t -----------------------------------------------------------------------
    """)
signal.signal(signal.SIGINT,capter_INT)
while True:

	cur = f"@server > "
	print(cur,end='',flush=True)

	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
	
	for notified_socket in read_sockets:
		
		if notified_socket == serversocket:
			
			client_socket, client_address = serversocket.accept()
			user = _message(client_socket)
			if user is False:
				break

			sockets_list.append(client_socket)
			clients[client_socket] = user
			pseudo_list.append(user['data'].decode('utf-8'))
			
			print("\nIncoming connection from {} on port {}...Username : {}".format(client_address[0],client_address[1],user['data'].decode('utf-8')))
			print("Liste des connectés : {}".format(pseudo_list))

		elif notified_socket == sys.stdin:

			mess_server = sys.stdin.readline()
			if mess_server:
				mg = mess_server[:-1]

				name = f"@server > ".encode('utf-8')
				
				m = mg.encode('utf-8')
				for client_socket in clients:
					client_socket.send(name + m)
			
			else:
				signal.signal(signal.SIGALRM,capter_ALRM)
				
		else:
			message_rec = _message(notified_socket)

			if message_rec is False:
				print("\nClosing connection from {}".format(clients[notified_socket]['data'].decode('utf-8')))
				sockets_list.remove(notified_socket)
				pseudo_list.remove(clients[notified_socket]['data'].decode('utf-8'))
				del clients[notified_socket]
				print("Liste des connectés : {}".format(pseudo_list))
					
				continue

			user = clients[notified_socket]
			msg = message_rec['data'].decode('utf-8')
			pseudo = ""
			for car in msg:
				if car == '_' or car == '@':
					continue
				elif car == ' ':
					break
				else:
					pseudo = pseudo + car
			print("\nReceived message from {} : {} ".format(user['data'].decode('utf-8'),msg))

			if msg.startswith('_@'):
				
				for client_socket in clients:
					if pseudo == clients[client_socket]['data'].decode('utf-8') and client_socket != notified_socket:

					 	x = message_rec['data']
					 	x_decod = x.decode('utf-8')
					 	split_x = x_decod.split()

					 	for mot in split_x:
					 		if mot.startswith('_@'):
					 			split_x.remove(mot)
					 	x_car = " ".join(split_x)
					 	msg_x = x_car.encode('utf-8')
					 	client_socket.send(user['header'] + user['data'] + message_rec['header'] + msg_x)

					if pseudo == "liste" and client_socket == notified_socket:
					 	list_conn = ", ".join(pseudo_list)
					 	list_encod = ("Liste des connectés :" + '[' + list_conn + ']').encode('utf-8')
					 	serve = "@server >".encode('utf-8')
					 	client_socket.send(user['header'] + user['data'] + message_rec['header'] + list_encod)
					
			else:
				for client_socket in clients:
					 if client_socket != notified_socket:
					 	client_socket.send(user['header'] + user['data'] + message_rec['header'] + message_rec['data'])

	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]

serversocket.close()