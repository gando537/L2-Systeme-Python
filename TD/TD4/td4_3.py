import os, sys, time , signal, errno

def handler(sig, ignore):
	cmpt = 0
	if cmpt < 6:
		cmpt += 1
	 	print("bip")
	 	signal.alarm(1)
	else:
		print("bye")
		sys.exit(0)


def signal_alarm():
	signal.signal(signal.SIGALRM, handler)
	while True:
		signal.alarm(1)

signal_alarm()