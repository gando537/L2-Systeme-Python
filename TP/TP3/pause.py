import time, signal, sys, os

def traitant(sig,ignore):
	print("\n\t\tMessage du traitant !")

if __name__ == '__main__':
	signal.signal(signal.SIGINT,traitant)
	print("\t\tpid = {}".format(os.getpid()))
	signal.pause()