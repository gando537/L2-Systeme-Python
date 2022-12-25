import os, sys, time , signal, errno

def my_handler1(sig, ignore):
	print("\nsignal {} reçu".format(sig))
	sys.exit(0)

def main():
	signal.signal(signal.SIGINT, my_handler1)
	#signal.signal(signal.SIGSTOP, my_handler1)
	#signal.signal(signal.SIGKILL, my_handler1)

	while True:
		signal.pause()
	sys.exit(0)

main()