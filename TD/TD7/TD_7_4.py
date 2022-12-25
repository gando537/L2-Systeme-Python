import sys,os,socket,time,select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_socket.bind(("",8801))
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
	    		m = msg.decode('utf-8')
	    		c = m.split()
	    		c_1 = c[0]
	    		a_1 = [c[1:]]
	    		c_2 = (c_1,c)
	    		c_3 = []
	    		c_3.append(c_2)
	    		c_4 , a_1 = c_3[0]
	    		if (len(m) == 0):
	    			print("NULL m. Closing connection...")
	    			sock_ready.close()
	    			socket_list.remove(sock_ready)
	    			nb_open -= 1
	    		else:
	    			pprint = os.execvp(c_4,a_1)
	    			server_socket.send(pprint)	
	            
server_socket.close()
print("last connection closed. Bye!")
sys.exit(0)







