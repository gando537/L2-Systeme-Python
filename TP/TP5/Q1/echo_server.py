import os,sys,atexit
import client_server

def _clean():
	global fifo_client
	try:
		print('Client --> {} : disconnected'.format(fifo_client))
		os.unlink("/tmp/ma_fifo1"+str(pid))
	except FileNotFoundError:
		pass

if __name__ == '__main__':

	atexit.register(_clean)
	pid = os.getpid()
	os.mkfifo("/tmp/ma_fifo1"+str(pid))
	rfd1 = os.open("/tmp/ma_fifo1"+str(pid), os.O_RDONLY)
	fifo_client = os.read(rfd1,1000)
	wfd2 = os.open(fifo_client, os.O_WRONLY)
	client_server.server(rfd1, wfd2)
	os.close(wfd2)
	sys.exit(0)
	




