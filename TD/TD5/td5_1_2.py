import os,sys,time,signal

def handler(sig,ignore):
	print("signal SIGUSR1 reçu !")
	sys.exit(0)

if __name__ == '__main__':

	pid = os.fork()
	if pid == 0:
		os.kill(os.getppid(),signal.SIGUSR1)
		sys.exit(0)
	else:
		signal.signal(signal.SIGUSR1,handler)
		os.wait()