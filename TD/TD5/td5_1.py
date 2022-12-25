import os,sys,time,signal

pid = os.fork()
if pid == 0:
	os.kill(os.getppid(),signal.SIGUSR1)
	sys.exit()
os.wait()
sys.exit()