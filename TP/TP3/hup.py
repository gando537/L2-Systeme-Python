import time, signal, sys, os

def capter_INT(sig,ignore):
	signal.SIG_IGN

if __name__ == '__main__':
	print(os.getpid())
	signal.signal(signal.SIGHUP, signal.SIG_IGN)
	while True:
		signal.pause()