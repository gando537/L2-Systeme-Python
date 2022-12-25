import time, signal, sys

def capter_INT(sig,ignore):
	signal.alarm(5)

def capter_alarm(sig,ignore):
	print("")
	sys.exit(0)

if __name__ == '__main__':
	
	signal.signal(signal.SIGINT, capter_INT)
	signal.signal(signal.SIGALRM, capter_alarm)
	while True:
		signal.pause()