import os, sys,signal,atexit
import select

_MAXBYTES = 1000

_SEPARATOR = ' '

def _clean():
    try:
        os.unlink("/tmp/ma_fifo2"+str(pid))
    except FileNotFoundError:
    	pass

def my_handler(sig,_):
	os.write(wfd, (myfifo + _SEPARATOR).encode('utf-8'))
	sys.exit(150)

def client(readfd, writefd, myfifo):
	while True:
		inputbuff = os.read(0, _MAXBYTES)            # lire contenu depuis entrée standard
		os.write(writefd, (myfifo + _SEPARATOR).encode('utf-8') + inputbuff)   # envoyer contenu sur tube vers serveur
		if len(inputbuff) == 0:
			break
		buff = os.read(readfd, _MAXBYTES)            #lire reponse serveur
		if len(buff) == 0:
			break
		os.write(1, buff)                            # ecrire contenu du fichier sur sortie standard



if __name__ == '__main__':
	if len(sys.argv) <= 1:
			print('Usage: {} expected 1 arg --> fifo_server'.format(sys.argv), file=sys.stderr)
			sys.exit(1)
	atexit.register(_clean)
	pid = os.getpid()
	arg = sys.argv[1:]
	fifo_server = arg[0]
	os.mkfifo("/tmp/ma_fifo2"+str(pid))
	fifo_client = "/tmp/ma_fifo2"+str(pid)
	wfd1 = os.open(fifo_server, os.O_WRONLY)
	os.write(wfd1,fifo_client.encode('utf-8'))
	rfd2 = os.open("/tmp/ma_fifo2"+str(pid), os.O_RDONLY)
	while True:
		active_readers, active_writers, _= select.select(0,fifo_client,[])
		for desc in active_readers:
			client(desc, wfd1,fifo_client)
	os.close(wfd1)
	sys.exit(0)






