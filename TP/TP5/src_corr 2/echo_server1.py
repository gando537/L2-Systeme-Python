import atexit, os, sys

_MAXBYTES = 1000

def server(readfd, writefd):
	while True:
		buff = os.read(readfd, _MAXBYTES)
		if len(buff) == 0:
			break
		os.write(writefd, buff)

def _clean(filename, wfd):
	print("clean-up", file=sys.stderr)
	os.close(wfd)
	try:
		os.unlink(filename)					 # faire le ménage sur disque.... 
	except FileNotFoundError:
		pass

if __name__ == '__main__':
	serverfifo = "/tmp/server" + os.path.basename(sys.argv[0]) + str(os.getpid())
	os.mkfifo(serverfifo)
	print('Fifo created:', serverfifo)
	rfd = os.open(serverfifo, os.O_RDONLY)
	wfd = os.open(os.read(rfd, _MAXBYTES).decode('utf-8'), os.O_WRONLY)
	atexit.register(_clean, serverfifo, wfd)
	server(rfd, wfd)
	sys.exit(0)
