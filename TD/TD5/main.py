import os,sys,client,server

if __name__ == "__main__":
	(rfd1,wfd1) = os.pipe() 
	(rfd2,wfd2) = os.pipe() 
	childpid = os.fork()
	if (childpid == 0): 
		os.close(wfd1) 
		os.close(rfd2)
		server.server(rfd1, wfd2)
		sys.exit(0) 
	os.close(rfd1) 
	os.close(wfd2)
	client.client(rfd2, wfd1) 
	os.waitpid(childpid, 0) 
	sys.exit(0)