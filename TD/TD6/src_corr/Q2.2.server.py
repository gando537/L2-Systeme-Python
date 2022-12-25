import os, sys

MAXLINE = 1000

def server(readfd, writefd):
	global MAXLINE
	buff = os.read(readfd, MAXLINE)
	try:
		fd = os.open(buff, os.O_RDONLY)
	except:
		os.write(writefd, b"error: can't open " + buff + b'\n')        
	else:
		# ouverture reussie
		buff = os.read(fd, MAXLINE)
		while len(buff) > 0:
			os.write(writefd, buff)
			buff = os.read(fd, MAXLINE)
		os.close(fd)

os.mkfifo("/tmp/ma_fifo1")
os.mkfifo("/tmp/ma_fifo2")
rfd1 = os.open("/tmp/ma_fifo1", os.O_RDONLY) # ouvre fifo1 en lecture
wfd2 = os.open("/tmp/ma_fifo2", os.O_WRONLY) # ouvre fifo2 en ecriture
server(rfd1, wfd2)
os.unlink("/tmp/ma_fifo1")         # faire le menage sur disque....
os.unlink("/tmp/ma_fifo2")
sys.exit(0)
