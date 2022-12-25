import time, signal, sys

def capter_INT(sig,ignore):
	print("Fini")
	sys.exit(0)
	signal.signal(sig_alarm, default_s)

if __name__ == '__main__':
	sig_alarm = signal.SIGALRM
	default_s = signal.alarm(5)
	signal.signal(sig_alarm, capter_INT)
	while True:
		time.sleep(1)
		print('Alives!')

