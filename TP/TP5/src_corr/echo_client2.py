import atexit, os, signal, sys

_MAXBYTES = 1000

_SEPARATOR = '¶'

def INT_handler(s, _):
	os.write(wfd, (myfifo + _SEPARATOR).encode('utf-8')) # envoyer message de deconnexion vers serveur
	sys.exit(130)

def client(readfd, writefd, myfifo):
	while True:
		inputbuff = os.read(0, _MAXBYTES) # lire contenu depuis entrée standard
		os.write(writefd, (myfifo + _SEPARATOR).encode('utf-8') + inputbuff) # envoyer contenu sur tube vers serveur
		if len(inputbuff) == 0:
			break
		buff = os.read(readfd, _MAXBYTES) # lire reponse serveur
		if len(buff) == 0:
			break
		os.write(1, buff)  # écrire contenu du fichier sur sortie standard

def _clean(filename, wfd):
	print("clean-up", file=sys.stderr)
	os.close(wfd)
	try:
		os.unlink(filename)
	except FileNotFoundError:
		pass

if __name__ == '__main__':
	signal.signal(signal.SIGINT, INT_handler)
	if len(sys.argv) < 2:
		print("usage: %s <server's fifo name>" % os.path.basename(sys.argv[0]), file=sys.stderr)
		sys.exit(1)
	myfifo = "/tmp/client" + os.path.basename(sys.argv[0]) + str(os.getpid())
	os.mkfifo(myfifo)
	wfd = os.open(sys.argv[1], os.O_WRONLY)
	atexit.register(_clean, myfifo, wfd)
	os.write(wfd, (_SEPARATOR + myfifo).encode('utf-8')) # write fifo name to server
	rfd = os.open(myfifo, os.O_RDONLY)
	client(rfd, wfd, myfifo)
	sys.exit(0)
