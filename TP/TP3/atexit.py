import time, signal, sys, atexit

def funct_message():
	print("Message de sorti !")
	sys.exit(0)

def myh(sig,ignore):
	funct_message()
	

if __name__ == '__main__':
	
	atexit.register(funct_message)
	signal.signal(signal.SIGINT, myh)
	signal.signal(signal.SIGABRT, myh)
	signal.signal(signal.SIGTERM, myh)
	signal.signal(signal.SIGQUIT, myh)
	signal.pause()
	