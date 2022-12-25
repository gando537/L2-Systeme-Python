import os, sys, time , signal, errno

counter = 0

def handler(sig, ignore):
	global counter
	counter += 1
	time.sleep(0.1)


def parent():
	signal.signal(signal.SIGUSR2, handler)

	try:
		os.wait()

	except:
		pass
	print("Counter = {}".format(counter))
	sys.exit(0)

def child():
	for i in range(5):
		os.kill(os.getppid(), signal.SIGUSR2)
		time.sleep(3)
		print("Sent SIGUSR2 to parent")
	sys.exit(0)

if __name__ == "__main__" :
	pid  = os.fork()
	if pid == 0 :
		child()
	else :
		parent()