import os,sys,time,signal

nb_sig = 0
def handler(sig,ignore):
	print("signal SIGUSR1 reçu !")
	#sys.exit(0)

if __name__ == '__main__':

	#global nb_sig
	parametre = int(sys.argv[1])
	pid = os.fork()
	if pid == 0:
		for i in range(1,parametre+1):
			os.kill(os.getppid(),signal.SIGUSR1)
			print("signal SIGUSR1 {} envoyé !".format(i))
		sys.exit(0)
	else:
		signal.signal(signal.SIGUSR1,handler)
		os.wait()