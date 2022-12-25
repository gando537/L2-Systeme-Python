import os, sys, time , signal, errno

def my_handler(sig, ignore):
	print("\n Le signal {} est en cours d'exécution".format(sig))

def pause() :
	signal.signal(signal.SIGINT, my_handler)
	while True:
		signal.pause()
	sys.exit(0)

pause()