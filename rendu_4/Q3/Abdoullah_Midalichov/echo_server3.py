import atexit, os, sys

_MAXBYTES = 1000

_SEPARATOR = '¶'

def register_client(client):
	print("new client registered:", client)
	wfd = os.open(client, os.O_WRONLY)
	writefds[client] = wfd

def unregister_client(client):
	print("client disconnected:", client)
	os.close(writefds[client])
	del writefds[client]

def server(readfd):
	
	while True:
		buff = os.read(readfd, _MAXBYTES)
		if len(buff) == 0:
			break
		text = buff.decode('utf-8')
		if text.startswith(_SEPARATOR):
			register_client(text[1:])
		else:
			client, text = text.split(_SEPARATOR)
			if text == '':
				unregister_client(client)
				continue
			for id_client in writefds:
				os.write(writefds[id_client], text.encode('utf-8'))

def _clean(filename):
	print("clean-up", file=sys.stderr)
	try:
		os.unlink(filename)					 # faire le ménage sur disque.... 
	except FileNotFoundError:
		pass

if __name__ == '__main__':
	writefds = {}
	serverfifo = "/tmp/server" + os.path.basename(sys.argv[0]) + str(os.getpid())
	os.mkfifo(serverfifo)
	print('Fifo created:', serverfifo)
	rfd = os.open(serverfifo, os.O_RDONLY)
	atexit.register(_clean, serverfifo)
	server(rfd)
	sys.exit(0)
