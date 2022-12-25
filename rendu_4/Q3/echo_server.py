import os,sys,atexit
import echo_client1

_MAXBYTES = 1000
_SEPARATOR = ' '

def _clean():
	global fifo_client
	try:
		print('Client --> {} : disconnected'.format(fifo_client))
		os.unlink("/tmp/ma_fifo1"+str(pid))
	except FileNotFoundError:
		pass

def fifoClient(file):
	fifo_client = ''
	message_gen_str = file.decode('utf-8')
	for car in message_gen_str:
		if car != _SEPARATOR:
			fifo_client = fifo_client + car
		else:
			break
	return fifo_client

def server(readfd, writefd):
	
	buff = os.read(readfd, _MAXBYTES)
	fifo_client = fifoClient(buff)
	x = len(fifo_client) + 1
	while len(buff) > 0:
		os.write(writefd, buff[x:])
		buff = os.read(readfd, _MAXBYTES)


if __name__ == '__main__':

	atexit.register(_clean)
	
	pid = os.getpid()
	os.mkfifo("/tmp/ma_fifo1"+str(pid))
	rfd1 = os.open("/tmp/ma_fifo1"+str(pid), os.O_RDONLY)
	message_gen = os.read(rfd1,1000)
	fifo_client = fifoClient(message_gen)
	wfd2 = os.open(fifo_client, os.O_WRONLY)
	server(rfd1, wfd2)
	sys.exit(0)
	




