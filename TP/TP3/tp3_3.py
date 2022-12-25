import time, signal, sys

def capter_INT(sig,ignore):
	signal.signal(sign, default_s)

if __name__ == '__main__':
	sign = signal.SIGINT
	default_s = signal.getsignal(sign)
	signal.signal(sign, capter_INT)
	while True:
		time.sleep(1)
		print('Alives!')
