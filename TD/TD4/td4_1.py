import os, sys, time , signal, errno

def handler(sig, ignore):
	print("\nCaught SIGINT")
	sys.exit(0)

signal.signal(signal.SIGINT, handler) # Met en place le nouveau traitant
signal.pause() #Attend la réception d'un signal
sys.exit(0)

