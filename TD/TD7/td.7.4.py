import sys,os,socket,time,select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_socket.bind(("",8803))
server_socket.listen(5)
nb_open = 0
# Create list of potential readers and place connection socket in 
# first position
socket_list = [server_socket]
first = True

while first or nb_open > 0:
    first = False 
    readers,_,_ = select.select(socket_list,[],[],60)
    
    for sock_ready in readers:
    	
    	if sock_ready == server_socket :
    		conn,(addr,port) = server_socket.accept()
    		socket_list.append(conn)
    		print("Incoming connexion from %s on port %d..."%(addr,port))
    		nb_open+=1
    	
    	else:
    		os.dup2(sock_ready.fileno(),1)
	    	os.dup2(sock_ready.fileno(),2)
	    	pid = os.fork()
    		if pid == 0:
	    		msg=sock_ready.recv(1024)
	    		message = msg.decode('utf-8')
	    		commande = message.split()
	    		commande1 = commande[0]
	    		argument1 = [commande[1:]]
	    		commande2 = (commande1,commande)
	    		commande3 = []
	    		commande3.append(commande2)
	    		commande4 , argument_1 = commande3[0]
	    		if (len(message) == 0):
	    			print("NULL message. Closing connection...")
	    			sock_ready.close()
	    			socket_list.remove(sock_ready)
	    			nb_open -= 1
	    		else:
	    			aff = os.execvp(commande4,argument1)
	    			server_socket.send(aff)
	            
server_socket.close()
print("last connection closed. Bye!")
sys.exit(0)







