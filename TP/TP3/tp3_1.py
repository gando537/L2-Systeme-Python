import time, signal, sys

def capter_INT(sig,ignore):
	pass
	

if __name__ == '__main__':
	signal.signal(signal.SIGINT,capter_INT)
	while True:
		time.sleep(1)
		print('Alives!')