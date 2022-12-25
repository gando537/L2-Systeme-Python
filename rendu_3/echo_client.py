import os,sys,atexit
import client_server

def _clean():
    try:
        os.unlink("/tmp/ma_fifo2"+str(pid))                         
    except FileNotFoundError:
        pass

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
	client_server.client(rfd2, wfd1)
	os.close(rfd2)
	sys.exit(0)
